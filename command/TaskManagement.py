import datetime
import discord
from discord.ext import commands, tasks
import command.db
from command.db import *
from command.model.DailyTask import *
from command.model.Task import *
from datetime import datetime, timedelta
import Paginator


async def check_tasks(channel,bot):
    now = datetime.now()
    now_time = now.strftime("%H:%M") 
    
    days_of_week = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"
    }
    days_of_weeks = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    print(f"🕒 Current time: {now_time}, Weekday: {now.weekday()}")  # Debug
    tasksList = command.db.getDailyTask(days_of_week[now.weekday()],now_time)
    if(tasksList != None):
        for task in tasksList:
            taskid = task["_id"]
            userid = task["userid"]
            task_name = task["name"]
            task_description = task["description"]
            task_time = task["time"]  
            task_dotw = task["dotw"] 
            dotw = days_of_weeks[task_dotw]
            if now.weekday() == dotw and now_time == task_time:
                await send_noti(channel,taskid,userid,task_name,task_description,task_time,bot)
    oneTimeTask = command.db.getOneDayTask(now_time)
    if(oneTimeTask != None):
        for task in oneTimeTask:
            taskid = task["_id"]
            userid = task["userid"]
            task_name = task["name"]
            task_description = task["description"]
            task_time = task["time"]
            if now_time == task_time:
                await send_one_time_noti(channel,taskid,userid,task_name,task_description,bot)


async def send_noti(channel,taskid ,userid, task_name, task_description,task_time,bot):
    user = await bot.fetch_user(userid)
    embed = discord.Embed(
        title="Daily Task Reminder!",
        description=f"```{task_name} - {task_description} - {task_time}```",
        colour=0xd4add7,
        timestamp=datetime.now()
    )
    embed.set_author(name=user.name)
    embed.set_thumbnail(url=user.avatar)
    embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")

    await channel.send(f"<@{user.id}>", embed=embed)  

async def send_one_time_noti(channel, taskid, userid, task_name, task_description, bot):
    user = await bot.fetch_user(userid)
    embed = discord.Embed(
        title="Your task is due!",
        description=f"```{task_name} - {task_description}```",
        colour=0xd4add7,
        timestamp=datetime.now()
    )

    class DoneButton(discord.ui.Button):
        def __init__(self, taskid):
            super().__init__(label="✅", style=discord.ButtonStyle.grey)
            self.taskid = taskid

        async def callback(self, interaction: discord.Interaction):
            command.db.deleteOneTimeTask(self.taskid)
            await interaction.response.send_message("✅ Task deleted!", ephemeral=True)

    class SnoozeButton(discord.ui.Button):
        def __init__(self, taskid):
            super().__init__(label="❌", style=discord.ButtonStyle.grey)
            self.taskid = taskid

        async def callback(self, interaction: discord.Interaction):
            now = datetime.now()
            new_time = (now + timedelta(minutes=5)).strftime("%H:%M") 
            command.db.updateOneTimeTask(self.taskid, new_time)
            await interaction.response.send_message(f"🔔 Task snoozed to {new_time}!", ephemeral=True)

    class TaskView(discord.ui.View):
        def __init__(self, taskid):
            super().__init__()
            self.add_item(DoneButton(taskid))  
            self.add_item(SnoozeButton(taskid)) 

    embed.set_author(name=user.name)
    embed.set_thumbnail(url=user.avatar)
    embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")

    await channel.send(f"<@{user.id}>", embed=embed, view=TaskView(taskid))



import Paginator
import discord
from discord.ext import commands, tasks
import command.db
from command.db import *
from command.model.DailyTask import *
from datetime import datetime, timedelta

async def getDailyTask(ctx,guildid):
    days_of_week = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    userid = ctx.author.id
    tasks = command.db.getSpecificUserDailyTasks(guildid,userid)

    if not tasks:  
        await ctx.send("No task found!")
        return

    embeds = []
    for i in range(7): 
        day = list(days_of_week.keys())[i]
        embed = discord.Embed(description=f"**{day} Tasks:**", colour=0x00b0f4)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")
        for task in tasks:
            if task.get("dotw") == day: 
                embed.add_field(name=task["name"]+ " - " + task["time"], value=task["description"], inline=False)

        embeds.append(embed)

    PreviousButton = discord.ui.Button(label="<", style=discord.ButtonStyle.gray)
    NextButton = discord.ui.Button(label=">", style=discord.ButtonStyle.gray)
    await Paginator.Simple(PreviousButton=PreviousButton, NextButton=NextButton).start(ctx, pages=embeds)


        
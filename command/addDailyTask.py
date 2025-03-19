import Paginator
import command
import command.TaskManagement
import command.db
from command.model.DailyTask import *
from discord import Intents, Client
from discord.ext import commands
from datetime import datetime
import discord

async def addDailyTask(ctx, guildid,task_info: str):
    try:
        userid = ctx.author.id
        task_info = task_info.split(' - ')
        name = task_info[0]
        description = task_info[1]
        time = task_info[2]    
        task = DailyTask(guildid,userid, name, description, time)
        command.db.addDailyTasks(task)
        embed = discord.Embed(title="Your task added succesful",
                        description="```"+task.__str__()+"```",
                      colour=0xd4add7,
                      timestamp=datetime.now())


        embed.set_thumbnail(url=ctx.author.avatar)

        embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")

        await ctx.reply(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send(f"An error occurred: {str(e)}")
        
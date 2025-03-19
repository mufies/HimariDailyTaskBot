import Paginator
import discord
from discord.ext import commands, tasks
import command.db
from command.db import *
from command.model.DailyTask import *
from datetime import datetime, timedelta

async def getTask(ctx, guildid):

    userid = ctx.author.id
    tasks = command.db.getSpecificUserOneTimeTasks(guildid,userid)

    if not tasks:  
        await ctx.send("No task found!")
        return
    embed = discord.Embed(description=f"**Today Tasks:**", colour=0x00b0f4)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")
    for task in tasks:
        embed.add_field(name=task["name"]+ " - " + task["time"], value=task["description"], inline=False)
    await ctx.reply(embed=embed)

        
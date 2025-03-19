import Paginator
import discord
from discord.ext import commands, tasks
import command.db
from command.db import *
from command.model.DailyTask import *
from datetime import datetime, timedelta

async def deleteSpecificDailyTask(ctx,guildid,userid,taskname):
    taskname = taskname.split(' - ')
    taskname1 = taskname[0]
    dotw = taskname[1]
    command.db.deleteSpecificUserDailyTask(guildid,userid,taskname1,dotw)
    await ctx.reply(f"Task {taskname} deleted successfully")

async def deleteSpecificTask(ctx,guildid,userid,taskname):
    command.db.deleteSpecificUserOneTimeTask(guildid,userid,taskname)
    await ctx.reply(f"Task {taskname} deleted successfully")
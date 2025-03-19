from discord import Intents, Client

from discord.ext import commands,tasks
import Paginator
import command
import command.TaskManagement
import command.addTask
from command.getDailyTask import *
from command.addDailyTask import *
from command.addTask import *
from command.getTask import *
from command.TaskManagement import *
import command.addDailyTask
import command.getDailyTask
import command.getTask
from command.model.DailyTask import *
from command.deleteSpecificTask import *



intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
prefix ='.' 
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('Himari to sensei: {:.2f} ms'.format(bot.latency *1000))

@bot.command()
async def addDailyTask(ctx, *, task_info: str):
    guildid = ctx.guild.id
    await command.addDailyTask.addDailyTask(ctx, guildid,task_info)
    


@bot.command()
async def getDailyTask(ctx):
    guildid = ctx.guild.id
    await command.getDailyTask.getDailyTask(ctx,guildid)

@bot.command()
async def addTask(ctx, *, task_info: str):
    guildid = ctx.guild.id
    await command.addTask.addTask(ctx, guildid,task_info)

@bot.command()
async def getTask(ctx):
    guildid = ctx.guild.id
    await command.getTask.getTask(ctx,guildid)

@bot.command()
async def deleteDailyTask(ctx, *, taskname: str):
    await deleteSpecificDailyTask(ctx,ctx.guild.id,ctx.author.id,taskname)

@bot.command()
async def deleteTask(ctx, *, taskname: str):
    await deleteSpecificTask(ctx,ctx.guild.id,ctx.author.id,taskname)    

@bot.command()
async def setchannel(ctx):
    channel = ctx.channel
    await ctx.send(f"📢 Channel set to: `{channel}`")
@tasks.loop(seconds=60)
async def loop():
    guilds = command.db.getGuilddb()
    for guild in guilds:
        channelid = guild["channelid"]
        guildid = guild["guildid"]
        channel = bot.get_channel(channelid)
        await command.TaskManagement.check_tasks(guildid,channel,bot)
        print(f"📢 Checking tasks for guild: {guildid}")
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    loop.start()  



@bot.command()
async def get_channel_id(ctx):
    await ctx.send(f"📢 Channel ID: `{ctx.channel.id}`")

token = ''

@bot.command()
async def pingme(ctx):
    delay = round(bot.latency * 5000)
    await ctx.send(f'📢 User '+ f'<@{ctx.author.id}>')

@bot.command()
async def setchannels(ctx):
    channelid = ctx.channel.id
    guildid = ctx.guild.id
    command.db.setGuildidAndChannelID(guildid,channelid)
    await ctx.reply(f"📢 Channel set to: `{ctx.channel}`")

@bot.event
async def on_guild_join(guild):
    system_channel = guild.system_channel
    if system_channel is not None:
        await system_channel.send("📢 Hello! I'm Himari, your personal task manager! Please enter the command:'.setChannel' to choose which channel i will use to remind you!")
    
bot.run(token)
from discord import Intents, Client

from discord.ext import commands,tasks
import Paginator
import command
import command.TaskManagement
from command.addTask import *
from command.TaskManagement import *
import command.addTask
from command.model.Task import *



intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
prefix ='.' 
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('Mika to sensei: {:.2f} ms'.format(bot.latency *1000))

@bot.command()
async def addTask(ctx, *, task_info: str):
    await command.addTask.addTask(ctx, task_info)
    


@bot.command()
async def getTasks(ctx):
    await command.TaskManagement.get_tasks(ctx)

@tasks.loop(seconds=60)
async def loop():
    channel = bot.get_channel(1239772586452189224)
    await command.TaskManagement.check_tasks(channel)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    loop.start()  
@bot.command()
async def get_channel_id(ctx):
    await ctx.send(f"📢 Channel ID: `{ctx.channel.id}`")
token = ''

bot.run(token)
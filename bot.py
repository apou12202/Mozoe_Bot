import discord
from discord.ext import commands
from discord.utils import get
from discord import Embed, Emoji
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='')  #set command title

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

#@bot.command()
#async def mozoe(ctx):


#bot.run(token) start
bot.run(jdata['TOKEN'])
import discord
from discord.ext import commands
from discord.utils import get
from discord import Embed, Emoji
import json
import random

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

with open('emoji.json', 'r', encoding='utf-8') as jemoji:
    jmoji = json.load(jemoji)

bot = commands.Bot(command_prefix='')  #set command title

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 貓肉(ctx):
    rnum = random.randint(0, len(jmoji['ming'])-1)
    await ctx.send(jmoji['ming'][rnum])
#bot.run(token) start
bot.run(jdata['TOKEN'])
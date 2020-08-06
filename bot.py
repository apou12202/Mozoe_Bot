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

@bot.event
async def on_message(message):
    # if message.content.find("5"):
    #     await message.channel.send("Hi")
    if message.content.startswith("那貓肉"):
        await message.channel.send(jmoji['ming'][random.randint(0, len(jmoji['ming'])-1)])
        print("on_message test")
    await bot.process_commands(message)   # https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 貓肉(ctx):
    # rnum = random.randint(0, len(jmoji['ming'])-1)
    await ctx.send(jmoji['ming'][random.randint(0, len(jmoji['ming'])-1)])
    print("貓肉emoji test")
#bot.run(token) start
bot.run(jdata['TOKEN'])
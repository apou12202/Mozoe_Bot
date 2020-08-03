import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')  #set command title

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

#bot.run(token) start
bot.run('NzM5ODY3OTQyMDA2NTU0Njg0.Xygttw.x3E3WwvY5QJ287BhZlyCQNJEVkI')


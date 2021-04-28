import discord
from discord.ext import commands, tasks
import os

bot = commands.Bot(command_prefix="!")
token = os.environ.get["TOKEN"]

@bot.event
async def on_ready():
    print("bot is online.")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(token)
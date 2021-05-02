# Im using replit cause its easier to use..
import discord
from discord.ext import commands, tasks
import os
import json # we will be needing this ltr.

bot = commands.Bot(command_prefix="!")
token = os.environ['TOKEN']
bot.remove_command('help') #also add this.
PREFIX = "+"

botName = "Tutorial Bot"
botInfo = "Tutorial Bot a bot made by Sn0wy1011#6779, with many commands!"
botAuthor = "Sn0wy1011#6779"
aGithub = "https://github.com/Snowy1011"
aIcon = "https://cdn.discordapp.com/avatars/805904764382609454/2033c7007c7463437777c764bc065ca7.webp"
botInvite = "https://discord.com/api/oauth2/authorize?client_id=835311237172691044&permissions=8&scope=bot"
bIcon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkqeSdKaOOy2j4Ds6B6XP-l7y_xE_xYWmfbOwyRbRmBvu-Z_8vfHZviNlwVYJMUZEvScI&usqp=CAU"

# this will print "Bot is online." to the console when it is online.
@bot.event
async def on_ready():
  print("Bot is online.")

# Ban Command
@bot.command(description="Ban Command!")
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, *, reason=None):
  embed=discord.Embed(title="Ban!", description=(f"Banned {member}"), color=0xb1acdd)
  embed.set_author(name=botAuthor, icon_url=aIcon)
  embed.set_thumbnail(url=bIcon)
  await member.ban(reason=reason)
  await ctx.send(embed=embed)
  print("Sent message for " + PREFIX + "ban")

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member, *, reason=None):
  await member.kick(reason=reason)
  embed=discord.Embed(title="Kick!", description=(f"Kicked {member}"), color=0xb1acdd)
  embed.set_author(name=botAuthor, icon_url=aIcon)
  embed.set_thumbnail(url=bIcon)
  await ctx.send(embed=embed)
  print("Sent message for " + PREFIX + "kick")

@bot.command()
@commands.has_permissions(administrator=True) # Will check if the person has adminstrator perms.
async def clear(ctx, amount=10000000000000000000000000000000000000000000000000000):
  # This is the set amount if u dont give an amount.
  await ctx.channel.purge(limit=amount) # This will clear the messages if not given a amount it will basically clear everything, but if there is an amount then it will clear that amount.
  print("Sent message for " + PREFIX + "clear")
  # Set Embed message.
  embed=discord.Embed(title="Clear", description="Cleared messages", color=0xb1acdd)
  embed.set_author(name=botAuthor, url=aGithub, icon_url=aIcon)
  embed.set_thumbnail(url=bIcon)
  await ctx.send(embed=embed)






  
  
  
  
  
  await ctx.channel.purge(limit=1)

@bot.command()
async def botinfo(ctx):
  embed=discord.Embed(title="Tutorial Bot", description="Tutorial bot is a bot made by Sn0wy1011#6779", color=0xb1acdd)
  embed.set_author(name=botAuthor, url=aGithub, icon_url=aIcon)
  await ctx.send(embed=embed)
  print("Sent message for " + PREFIX + "botinfo")

@bot.command()
async def help(ctx):
  embed=discord.Embed(title="Help", url=botInvite, description="**Commands:**", color=0xb1acdd)
  embed.set_author(name=botAuthor, url=aGithub, icon_url=aIcon)
  embed.set_thumbnail(url=bIcon)
  embed.add_field(name="Moderation:", value="``Kick``, ``Ban``, ``Clear``", inline=True)
  embed.add_field(name="Music:", value="``More coming soon``", inline=False)
  embed.add_field(name="Info:", value="``botinfo``")
  await ctx.send(embed=embed)
  print("Sent message for " + PREFIX + "help")
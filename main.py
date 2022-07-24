import os
import sys
import discord
import traceback
from pathlib import Path
from colorama import Fore
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["-"],intents=intents,activity=discord.Activity(type=discord.ActivityType.listening, name="To The Almighty Thug Lord"))


@bot.event
async def on_ready():
  print(Fore.MAGENTA + "========[ " + bot.user.name + " is Online! ]========" + Fore.RESET)
  print(Fore.RED + "========[ Discord Version: " + discord.__version__ + " ]=======")
      
bot.run(os.getenv("TOKEN"))

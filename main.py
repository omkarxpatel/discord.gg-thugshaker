import os
from discord.ext import commands

bot = commands.Bot(command_prefix=["-"],intents=intents,activity=discord.Activity(type=discord.ActivityType.listening, name="To The Almighty Thug Lord"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))

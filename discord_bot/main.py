import os
import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

discord_token = os.environ['DISCORD_TOKEN']

@bot.command()
async def inverse(ctx, message):
    await ctx.send(message[::-1])

bot.run(discord_token)
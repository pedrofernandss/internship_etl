import asyncio
import os
import discord 
from discord.ext import commands

discord_token = os.environ['DISCORD_TOKEN']
channel_id = int(os.environ['CHANNEL_ID'])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def send_scheduled_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    while not bot.is_closed():
        await asyncio.sleep(2)
        await channel.send("Mensagem programada!")
        
@bot.event
async def on_ready():
    bot.loop.create_task(send_scheduled_message())

bot.run(discord_token)
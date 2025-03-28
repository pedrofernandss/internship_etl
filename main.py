import asyncio
import os
import discord 
from discord.ext import commands

from remotar_jobs.intern.main import clean_data, get_jobs

discord_token = os.environ['DISCORD_TOKEN']
channel_id = int(os.environ['CHANNEL_ID'])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def send_scheduled_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    while not bot.is_closed():
        jobs = get_jobs()
        new_jobs_messages = clean_data(jobs)
        
        for job_message in new_jobs_messages:
            await channel.send(job_message)
        
        if not new_jobs_messages:
            print("Nenhuma vaga nova encontrada.")
        
@bot.event
async def on_ready():
    bot.loop.create_task(send_scheduled_message())

bot.run(discord_token)
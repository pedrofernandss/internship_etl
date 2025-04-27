import asyncio
import os
import discord 
from discord.ext import commands

from internship.sites.remotar import clean_data

discord_token = os.environ['DISCORD_TOKEN']
channel_ids = [int(id_) for id_ in os.environ['CHANNEL_IDS'].split(',')]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def send_scheduled_message():
    await bot.wait_until_ready()
    channels = [bot.get_channel(id_) for id_ in channel_ids]

    while not bot.is_closed():
        new_jobs = clean_data()

        if new_jobs:
            for job in new_jobs:
                job_message = (
                f"✨ **Nova vaga disponível!** ✨\n\n"
                f"A empresa **{job['company_name']}** abriu uma nova vaga\n\n"
                f"🧑‍🎓 Nível: **Estágio**\n"
                f"📌 Cargo: **{job['title']}**\n"
                f"📍 Localidade: **Remoto**\n"
                f"🔗 [Acesse a vaga aqui]({job['link']})\n\n" 
                f"Caso decida se inscrever, não esqueça de personalizar seu currículo! 😉\n"
                )
                await channels.send(job_message)
                await asyncio.sleep(60)

        await asyncio.sleep(3600) 
                
@bot.event
async def on_ready():
    bot.loop.create_task(send_scheduled_message())

bot.run(discord_token)
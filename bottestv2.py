import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client  discord.Client()
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    print('thx')
@client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg = 'hello {0.author.mention} how are you'.foarmat(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('.bye'):
        msg = 'bye {0.author.mention} bye'.foarmat(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))

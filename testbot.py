import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Grand Theft Auto X'))
    await client.send_message(member, 'eyyy tanks for joining')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '+ping':
        await client.send_message(message.channel,'pong')
    if message.content == '+imgboi':
        em = discord.Embed(description='O.K')
        em.set_image(url='https://i.imgflip.com/2o0f7m.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('+coinflip'):
        randomlist = ["pladt","krone",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '+pingme':
        await client.send_message(message.channel,'nej. <@%s>')
client.run('NTE5NTcxMjc2MDYzNTcxOTc4.DuhQEQ.5a0bzrOR9DnvFv-vI34kwn9Zvfk')

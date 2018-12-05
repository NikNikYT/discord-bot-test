import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'hej og velkommen')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='ost'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '+commands':
        await client.send_message(message.channel,'all the commands havent yeet been added')
    if message.content == '+imgboi':
        em = discord.Embed(description='where is my $40 bill XD')
        em.set_image(url='https://i.imgflip.com/2o1kfo.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('+er du god eller ond'):
        randomlist = ["ja","nej","hvem ved","måske","hey se der er en fugl",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '+ny test':
        await client.send_message(message.channel,'test virker')
client.run(os.getenv('TOKEN'))

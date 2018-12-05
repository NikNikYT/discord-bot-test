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
    if message.content.startswith('+pingmebitch'):
        await client.send_message(message.channel,'its try me bitch <@%s>'  %(message.author.id))
    if ('fuck dig bitch') in message.content:
       await client.delete_message(message)
    if message.content == '+fav sang':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=-yHoa4MR0W4 her')
    if message.content.startswith('+8ball'):
        randomlist = ["du er heldig resten af dagen","du kommer til at dø ung","vidste du vis du spiser for meget kage så bliver du fed?","10 minuter mere mor.","prøv senere","jeg har en mega hovedet pine så gå plz","shaun mendes er grim XD","måske","hvem ved","sikkert","er ikke sikker"]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run(os.getenv('TOKEN'))

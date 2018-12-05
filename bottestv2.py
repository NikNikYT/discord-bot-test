import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
import youtube_dl
from discord import Game

players = {}

client = commands.Bot(command_prefix = '+')
Clientdiscord = discord.Client()
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='you sleep.', type = 3))
    print('Bot Online.')



@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
        id = ctx.message.server.id
        players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command()
async def ping():
    await client.say("pong")

@client.command()
async def pong():
    await client.say("ping")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
          colour = discord.Colour.blue()
    )

    embed.set_author(name="help")
    embed.add_field(name="+ping", value="Returns Pong!", inline=False)
    embed.add_field(name="+pong", value="Returns Ping!", inline=False)
    embed.add_field(name="+join", value="joins the voice channel you are in", inline=False)
    embed.add_field(name="+leave", value="leaves the voice channel", inline=False)
    embed.add_field(name="+play [Youtube link]", value="plays the music you put in [virker ikke]", inline=False)
    embed.add_field(name="+pause", value="pauses the music [virker ikke]", inline=False)
    embed.add_field(name="+resume", value="resumes the music [virker ikke]", inline=False)
    embed.add_field(name="+stop", value="stops the music completly [virker ikke]", inline=False)

    await client.send_message(author, embed=embed)

client.run(os.getenv('TOKEN'))

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
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

client = commands.Bot(command_prefix = '+')
Clientdiscord = discord.Client()
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='+help'))
    print('Bot Online.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say("Joined.")

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("Left.")

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()
    await client.say("Playing Now.")

@client.command(pass_context=True)
async def pause(ctx):
        id = ctx.message.server.id
        players[id].pause()
        await client.say("Paused.")

@client.command(pass_context=True)
async def skip(ctx):
    id = ctx.message.server.id
    players[id].stop()
    await client.say("Skipped.")

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await client.say("Resumed.")

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
        await client.say("Video queued.")

@client.command()
async def ping():
    await client.say("pong!")

@client.command()
async def pong():
    await client.say("ping!")

@client.command()
async def version():
    await client.say("The Bot is in Version 1.3 Beta")

@client.command()
async def credits():
    await client.say("Coder and Head-Developer: a random person#4629")
    await client.say("Co-Developer: 𝓣𝓱𝓮 𝓓𝓪𝓷𝓲𝓼𝓱 𝓦𝓸𝓵𝓯#9077")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
          colour = discord.Colour.blue()
    )

    embed.set_author(name="help")
    embed.add_field(name="+ping", value="Returns Pong!", inline=False)
    embed.add_field(name="+pong", value="Returns Ping!", inline=False)
    embed.add_field(name="+join", value="Joins the voice channel you are in", inline=False)
    embed.add_field(name="+leave", value="Leaves the voice channel", inline=False)
    embed.add_field(name="+play [Youtube link]", value="Plays the music you put in", inline=False)
    embed.add_field(name="+queue [Youtube link]", value="Adds the music to the queue", inline=False)
    embed.add_field(name="+pause", value="Pauses the music", inline=False)
    embed.add_field(name="+resume", value="Resumes the music", inline=False)
    embed.add_field(name="+skip", value="Skips to the next Song in the queue", inline=False)
    embed.add_field(name="+version", value="Displays what version we are in", inline=False)
    embed.add_field(name="+credits", value="Tells you who the makers are", inline=False)

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
@commands.has_role("Owners")
async def clear(ctx, amount=5):
    await client.purge_from(ctx.message.channel,limit=amount)

client.run(os.getenv('TOKEN'))


import discord
from discord.ext import commands
from discord.ext import tasks
import os
import glob, random
from PIL import Image, ImageDraw, ImageSequence,ImageFont
from textwrap import wrap
client = commands.Bot(command_prefix="+")
custom_emojis = [
    "mmlao",
    "chadStu",
    "ElChadmo",
    "VirginStu"
]
token = "ODY0OTQzMzc2NjM3NzU1Mzkz.YO8zSg.J9DuJGoEAvsKBQX12ZG5b_jNvWA"
async def react(message):
    #for emoji in default_emojis:
        #await message.add_reaction(emoji)
    for emoji in message.guild.emojis:
        if emoji.name in custom_emojis:
            await message.add_reaction(emoji)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "mlao" in message.content.lower():
        await react(message)
        
        
client.run(token)
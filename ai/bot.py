import asyncio
import aiohttp
import discord

import re
import requests

from discord import Client
import os
from dotenv import load_dotenv

BASEDIR = os.getcwd()
load_dotenv((os.path.join(BASEDIR, '.env')))
key = os.getenv("DISCORD_TOKEN")

class Test_Client(discord.Client):
    try:
        async def on_ready(self):
            #print(f'User: {self.user}')
            for guild in client.guilds:
                for channel in guild.channels:
                    pass
                    #print(channel, channel.permissions_for)
        async def on_message(self, message):
            if message.author.id != self.user.id:
                print(message.content)
                #further idiot-proof this?
                regmatch = re.compile('https://tinyurl.bridgebase.com/[\w]{8}')
                link = re.search(regmatch, message.content)
                if link is not None:
                    print(link.group(0))
                    response = requests.get(link.group(0))
                    print(response.text)
            if message.author.name   == "jgillispie":
                await message.reply("Hi! Right now I don't say very much, but one day soon I will!")
                
    except Exception as e:
      print(e)  

client = Test_Client(intents=discord.Intents.all())
client.run(token=key, reconnect=True)



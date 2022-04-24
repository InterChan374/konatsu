import discord
import logging
import json
from os.path import exists

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

knowers_blacklist = []
if exists("knowers_blacklist.json"):
    with open("knowers_blacklist.json", "r") as knowers_blacklist_file:
        knowers_blacklist = json.load(knowers_blacklist_file)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "toggle know'ers":
        if message.channel.id in knowers_blacklist:
            # remove from blacklist to enable
            knowers_blacklist.remove(message.channel.id)
            await message.channel.send(f"enabled know'ers here (channel id {message.channel.id})")
        else:
            # add to blacklist to disable
            knowers_blacklist.append(message.channel.id)
            await message.channel.send(f"disabled know'ers here (channel id {message.channel.id})")
        with open("knowers_blacklist.json", "w") as knowers_blacklist_file:
            json.dump(knowers_blacklist, knowers_blacklist_file)


    if message.channel.id not in knowers_blacklist:
        words = message.content.split()
        knowners = []
        for word in words:
            if "er" in word.lower() and word not in knowners:
                knowners.append(word)
                await message.channel.send(f"{word.capitalize()}? I 'ardly know 'er{word.lower().split('er')[-1]}!")

with open("token.xd", "r") as xd:
    client.run(xd.read())
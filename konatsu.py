import discord
import logging
import json
from os.path import exists
from discord.ext import commands

logging.basicConfig(level=logging.ERROR)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

knowers_whitelist = []
if exists("knowers_whitelist.json"):
    with open("knowers_whitelist.json", "r") as knowers_whitelist_file:
        knowers_whitelist = json.load(knowers_whitelist_file)

chain_content = ""
chain_counter = 0
chain_sentcount = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}\n')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # toggle know'ers
    if message.content == "toggle know'ers":
        if message.channel.id in knowers_whitelist:
            # remove from whitelist to disable
            knowers_whitelist.remove(message.channel.id)
            await message.channel.send(f"*disabled know'ers here (channel id {message.channel.id})*")
        else:
            # add to whitelist to enable
            knowers_whitelist.append(message.channel.id)
            await message.channel.send(f"*enabled know'ers here (channel id {message.channel.id})*")
        with open("knowers_whitelist.json", "w") as knowers_whitelist_file:
            json.dump(knowers_whitelist, knowers_whitelist_file)
    
    # i hardly know'er detector
    if message.channel.id in knowers_whitelist:
        words = message.content.split()
        knowners = []
        for word in words:
            if "er" in word.lower() and word not in knowners:
                knowners.append(word)
                await message.channel.send(f"{word.capitalize()}? I 'ardly know 'er{word.lower().split('er')[-1]}!")
    
    # message chain joiner
    global chain_content
    global chain_counter
    global chain_sentcount
    if message.content == chain_content:
        # it is indeed the same as the previous message
        chain_counter += 1
        if chain_counter > chain_sentcount + 1:
            await message.channel.send(chain_content)
            chain_counter = 0
            chain_sentcount += 1
    else:
        chain_content = message.content[:]
        chain_counter = 0
        chain_sentcount = 0

with open("token.xd", "r") as xd:
    bot.run(xd.read())

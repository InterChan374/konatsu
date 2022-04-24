import discord
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.split()
    for word in words:
        if word.endswith("er"):
            await message.channel.send(f"{word.capitalize()}? I hardly know 'er!")

client.run(open("token.xd", "r").read())
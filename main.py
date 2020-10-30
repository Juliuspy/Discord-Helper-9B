import discord
from discord.ext import commands

print("Version is:", discord.__version__)

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "hallo" in message.content.lower():
        await message.channel.send("HI!")

        if "Hi" in message.content.lower():
            await message.channel.send("HI!")

        if "hi" in message.content.lower():
            await message.channel.send("HI!")
        if "moin" in message.content.lower():
            await message.channel.send("HI!")
        if on_member_join(member):
            await user.send("Willkommen auf dem Discord-Server der 9B!")



client.run(token)

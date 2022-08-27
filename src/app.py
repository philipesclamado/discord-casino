import discord
import os

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('a user connected to {0.user}'.format(client))


def run():
    client.run(os.environ['TOKEN'])



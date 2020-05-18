import discord

TOKEN = None

client = discord.Client()


def run():
    client.run(TOKEN)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().contains('salvo'):
        response = "Currently building our artillery batteries, sir."
        await message.channel.send(response)
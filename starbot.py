import discord
from discord.ext import commands
import random
import time

act = discord.Activity(name="Always ready to serve.")
TOKEN = "NzExNjM0MjM4NzM0MzM2MDMx.XsHkhQ.CbdWWf9gQgqoZ2_qx0KFXDM0LBU"
client = discord.Client()
bot = commands.Bot(command_prefix='!', activity=act)

@client.event
async def on_message(message):
    if message.content.startswith('salvo'):
        time.sleep(2)
        text = "\t\t\t. /\n" \
               "   _ - | -- -= *:--\n" \
               "._(O) /        ' `\n"
        await message.channel.send('SALVO!')
        time.sleep(2)
        await message.channel.send(text)
        time.sleep(2)
        await message.channel.send("......")
        time.sleep(2)
        await message.channel.send("......")
        time.sleep(2)
        await message.channel.send("......")
        time.sleep(1)
        text =  "\t'.  \ | /  ,'\n"\
        " ( .`.|,' .)\n"\
        "- ~ -0- ~ -"


@bot.command(name='roll')
async def roll(ctx, number_of_sides):
    try:
        number_of_sides = int(str(number_of_sides[1]) + str(number_of_sides[2]))
    except IndexError:
        print("error")
        number_of_sides = int(str(number_of_sides[1]))
    finally:
        dice = str(random.choice(range(1, number_of_sides + 1)))
        await ctx.channel.send(dice)

def run():
    client.run(TOKEN)
    bot.run(TOKEN)
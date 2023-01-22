#import lib for bot
import disnake
import discord

import datetime

#import os lib for security
import os

from dotenv import load_dotenv
load_dotenv()
from disnake.ext import commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
user = disnake.Message.author
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)
game = disnake.Game("API")

# Когда бот будет готов, эта функция будет запущена.
@bot.event
async def on_ready():
    await bot.change_presence(status=disnake.Status.do_not_disturb, activity=game)
    print("Bot is ready!")

@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Понг!")

@bot.slash_command()
async def fullembed(inter):

    embed = disnake.Embed(
    title="Welcome to 'whyalive? Support Server'",
    description="This server was made to help you to interact with this bot",
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
    )

    embed.set_author(
    name= "whyalive?",
    url="https://github.com/malberecode",
    )

    embed.set_footer(
    text="made by: malbere_team"
    )

    await inter.response.send_message(embed=embed)
    print("Embed was send!")


# Войдите в Discord с помощью токена бота.
bot.run(TOKEN)
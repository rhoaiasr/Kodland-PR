import discord
from choiceimage import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    
@bot.command()
async def meme(ctx):
    with open (choicememes(), "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
token = ''
bot.run(token)
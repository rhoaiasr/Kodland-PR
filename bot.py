import discord
from discord.ext import commands
from funciones import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready ():
    print (f"We have logged in as {bot.user}")

@bot.command()
async def descomponer (ctx,*, objeto:str):
    #llamar a la funcion
    result = tiempo_descomp(objeto)

    #Enviar respuesta
    await ctx.send(result)

token = ""
bot.run (token)
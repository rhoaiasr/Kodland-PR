import discord # Importando la libreria discord
from password import gen_pass #Importando la funcion de otro archivo de codigo

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$psw"):
        await message.channel.send("Aqui tienes la contraseña:" + gen_pass(8)) #Funcion de otro archivo de codigo
    else:
        await message.channel.send(message.content)

token = ""

client.run (token)
import discord
import json
import random
import asyncio
from discord.ext import commands
import os

#client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

with open("config.json") as f:
    data = json.load(f)

interval=data["interval"]

@client.event
async def on_ready():
    print('Logueado como: {0.user}'.format(client))
    sincro=await client.tree.sync()
    print("Comandos sincronizados "+str(len(sincro)))
   
@client.tree.command(name="rol_arcoiris",description="Este comando hace que un rol parsado cambie de color constantemente")
async def rol(interaction:discord.Interaction,role:discord.Role):
    await interaction.response.send_message(content="Canbiando de color el rol "+str(role))
    async def cambiar_color_rol():
        while True:
            r = random.randint(0,0xFFFFFF)
            await role.edit(color=discord.Colour(r))
            await asyncio.sleep(interval/1000)
    client.loop.create_task(cambiar_color_rol())

@client.tree.command(name="test",description="Esto es un test")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")


#for f in os.listdir('./fun'):
#    if f.endswith('.py'):
#        client.load_extension(f'cogs.{f[:-3]}')
token=data["token"]
client.run(token)

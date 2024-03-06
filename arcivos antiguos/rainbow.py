import discord
import json
import random
import asyncio
from discord.utils import get

client = discord.Client(intents=discord.Intents.all())

with open("config.json") as f:
    data = json.load(f)

interval=data["interval"]
serverID=data["serverID"]
roleID=data["roleID"]
@client.event
async def on_ready():
    print('Logueado como: {0.user}'.format(client))
    server=client.get_guild(serverID)
    #server=discord.utils.get(client.guilds,id=serverID)
    #rol=discord.utils.get(server, id=roleID)
    rolesA=server.get_role(roleID)
    async def cambiar_color_rol():
        while True:
            r = random.randint(0,0xFFFFFF)
            await rolesA.edit(color=discord.Colour(r))
            await asyncio.sleep(interval/1000)
    #client.loop.create_task(cambiar_color_rol())
    await cambiar_color_rol()


token=data["token"]
client.run(token)
import discord
from discord import app_commands
from discord.ext import commands
import os
import random
import requests
import json
import asyncio
import mysql.connector
db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1234",
                                     database="discord",
                                     port=3306,
                                     autocommit=True
                                    )
cursor = db.cursor(dictionary=True)
class Testeos2(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        
        
    @app_commands.command(name="rol_arcoiris3",description="Este comando hace que un rol parsado cambie de color constantemente")
    async def rol(self,interaction:discord.Interaction,role:discord.Role):
        await interaction.response.send_message(content="Canbiando de color el rol")
        
        async def cambiar_color_rol():
            interval=60000
            while True:
                r = random.randint(0,0xFFFFFF)
                await role.edit(color=discord.Colour(r))
                await asyncio.sleep(interval/1000)
        commands.Bot.loop.create_task(cambiar_color_rol())
    @app_commands.command(name="meme",description="Genera un meme aleatorio (Puede ser en ingles)")
    async def meme(self,interaction:discord.Interaction):
        #memeapi="https://meme-api.com/gimme/1"
        r = requests.get(r'https://meme-api.com/gimme').text
        meme= json.loads(r)
        embed = discord.Embed(color=discord.Colour.random()).set_image(url=f"{meme['url']}")
        await interaction.response.send_message(embed=embed)
        
        #content = requests.get("https://meme-api.com/gimme").text
        #data = json.loads(content)
        #embed = discord.Embed(title=f"{data['title']}", color=discord.Colour.random()).set_image(url=f"{data['url']}")
        #await interaction.response.send_message(embed=embed)

        #await interaction.response.send_message(content=meme)
    @app_commands.command(name="stop_arcoiris",description="Para el cambio de color de un rol")
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def stop_arcoiris(self,interaction:discord.Interaction,rolq:discord.Role):
        cursor.execute(f"SELECT idRol FROM rolRainbow WHERE idRol ={rolq.id};")
        lista= [int(i['idRol']) for i in cursor.fetchall()]
        if len(lista) > 0:
            cursor.execute(f"DELETE FROM rolRainbow WHERE idRol = {rolq.id}")
            await interaction.response.send_message(content=f"Rol {rolq.mention} parado correctamente")
        else:
            await interaction.response.send_message(content=f"{rolq.mention} no se esta cambiando de color")



async def arcoiris(self):
        interval=60000
        while True:
            cursor.execute(f"SELECT id FROM servidores;")
            lista= [int(i['id']) for i in cursor.fetchall()]
            if estaVacio(lista)==False:
                for servidor in lista:
                    cursor.execute(f"SELECT idRol FROM rolRainbow WHERE idServidor = {servidor};")
                    roles=[int(i['idRol']) for i in cursor.fetchall()]
                    if estaVacio(roles)==False:
                        for rol in roles:
                            print(f'{str(rol)}')
                            await cambiarColor(self,rol,servidor)
                await asyncio.sleep(interval/1000)
async def cambiarColor(self,idRol,idServidor):
    server=self.get_guild(idServidor)
    role=server.get_role(idRol)
    r = random.randint(0,0xFFFFFF)
    await role.edit(color=discord.Colour(r))

    



    

def estaVacio(list):
     return not bool(list)

async def setup(bot:commands.Bot):
    #for f in os.listdir('./diversion'):
    #        if f.endswith('.py'):
    #            await bot.load_extension(f'diversion.{f[:-3]}')
    await bot.add_cog(Testeos2(bot))
        
def mirar():
    print("Hola que tal")


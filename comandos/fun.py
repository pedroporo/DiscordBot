import discord
from discord import app_commands
from discord.ext import commands
import os
import random
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

async def arcoiris():
    interval=60000
    cursor.execute(f"SELECT rolId FROM rolRainbow;")
    roles=[int(i['rolId']) for i in cursor.fetchall()]
    cursor.execute(f"SELECT id FROM servidores;")
    servidores= [int(i['id']) for i in cursor.fetchall()]

    while True:
            r = random.randint(0,0xFFFFFF)
            await role.edit(color=discord.Colour(r))
            await asyncio.sleep(interval/1000)
async def setup(bot:commands.Bot):
    #for f in os.listdir('./diversion'):
    #        if f.endswith('.py'):
    #            await bot.load_extension(f'diversion.{f[:-3]}')
    await bot.add_cog(Testeos2(bot))
        
def mirar():
    print("Hola que tal")


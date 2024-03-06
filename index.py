import discord
import random
import asyncio
from discord.ext import commands
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
#client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1234",
                                     database="discordtest",
                                     port=3306,
                                     autocommit=True
                                    )
cursor = db.cursor(dictionary=True)



interval=60000

@client.event
async def on_ready():
    print('Logueado como: {0.user}'.format(client))
    for f in os.listdir('./comandos'):
        if f.endswith('.py'):
            await client.load_extension(f'comandos.{f[:-3]}')
    sincro=await client.tree.sync()
    print("Comandos sincronizados "+str(len(sincro)))
   
@client.tree.command(name="rol_arcoiris",description="Este comando hace que un rol parsado cambie de color constantemente")
async def rol(interaction:discord.Interaction,role:discord.Role):
    await interaction.response.send_message(content="Canbiando de color el rol")
    async def cambiar_color_rol():
        while True:
            r = random.randint(0,0xFFFFFF)
            await role.edit(color=discord.Colour(r))
            await asyncio.sleep(interval/1000)
    client.loop.create_task(cambiar_color_rol())

@client.tree.command(name="test",description="Esto es un test")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

@client.tree.command(name="reporte",description="Comando usado por administradores para registrar el mal comportamiento de los usuarios")
async def reporte(interaction:discord.Interaction,usuario:discord.User,infraccion_cometida:str="Texto por defecto"):
    await interaction.response.send_message(f"Reporte al usuario {usuario.display_name} completada")

    cursor.execute(f"INSERT INTO `mensaje`(`channel_id`,`id_afectado`, `message`) VALUES ('{interaction.channel_id}','{usuario.id}', '{infraccion_cometida}')")

@client.tree.command(name="verreportes",description="Comando usado por administradores para ver el mal comportamiento de los usuarios")
async def verreporte(interaction:discord.Interaction,usuario:discord.User):
    cursor.execute(f"SELECT message FROM mensaje WHERE id_afectado = {usuario.id};")
    infracciones=[i['message'] for i in cursor.fetchall()]
    mbed = discord.Embed(
       title=f"Infracciones de {usuario.display_name}",
       colour=(discord.Colour.green())
    )
    mbed.add_field(name="Lista",value='\n'.join(infracciones),inline=True)
    await interaction.response.send_message(embed=mbed)

def getServers():
    cursor.execute(f"SELECT id FROM servidores;")
    lista= [int(i['id']) for i in cursor.fetchall()]
    print(lista)
    
    for servidor in client.guilds:
        print(f"ID= {servidor.id} , Nombre={servidor.name}")
        #cursor.execute(f"SELECT id FROM servidores WHERE id = {servidor.id};")
        #lista= [int(i['id']) for i in cursor.fetchall()]
        if servidor.id not in lista:
            cursor.execute(f"INSERT INTO `servidores`(`id`,`nombre`) VALUES ('{servidor.id}','{servidor.name}')")


@client.tree.command(name="recargarcomandos",description="Recarga los comandos del bot")
@commands.has_permissions(administrator=True)
async def recargarcomandos(interaction:discord.Interaction):
    try:
        for f in os.listdir('./comandos'):
            if f.endswith('.py'):
                await client.unload_extension(f'comandos.{f[:-3]}')
                await client.load_extension(f'comandos.{f[:-3]}')
        # Alerts the chat where the command was sent, that the Cog has been reloaded.
        await interaction.response.send_message(f"Reinicio completado.", delete_after=10)
    except Exception as e:
        channel = client.get_channel(675360472622432291)
        await channel.send(f"Hubo un error en el recargo, reinicia el bot completamente. <@&332459579789017091>")
        raise e
@client.command()
#@commands.has_permissions(administrator=True)
@commands.is_owner()
async def reload(ctx, cog):
    try:
        client.unload_extension(f"comandos.{cog}")
        client.load_extension(f"comandos.{cog}")
        # Alerts the chat where the command was sent, that the Cog has been reloaded.
        await ctx.send(f"{cog} has been reloaded.", delete_after=10)
    except Exception as e:
        channel = client.get_channel(675360472622432291)
        await channel.send(f"Cog: {cog} did not start up properly, restart the bot completely. <@&332459579789017091>")
        raise e
    
@client.command()
@commands.is_owner()
async def reloadAll(ctx):
    try:
        for f in os.listdir('./comandos'):
            if f.endswith('.py'):
                await client.unload_extension(f'comandos.{f[:-3]}')
                await client.load_extension(f'comandos.{f[:-3]}')
        # Alerts the chat where the command was sent, that the Cog has been reloaded.
        await ctx.send(f"Reinicio completado.", delete_after=10)
    except Exception as e:
        channel = client.get_channel(675360472622432291)
        await channel.send(f"Hubo un error en el recargo, reinicia el bot completamente. <@&332459579789017091>")
        raise e



token=os.getenv('TOKEN')
client.run(token)
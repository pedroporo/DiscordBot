import discord
import json
import random
import asyncio
from discord.ext import commands
import mysql.connector
import os

with open("config.json") as f:
    data = json.load(f)

interval=data["interval"]

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

@client.event
async def on_ready():
    print('Logueado como: {0.user}'.format(client))
    print("Servidores connectados:")
    getServers()

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
        

token=data["token"]
client.run(token)
import discord
import os
import mysql.connector
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$reporte'):
        await message.channel.send('Ok')

        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1234",
                                     database="discordtest",
                                     port=3306,
                                     autocommit=True
                                    )
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"INSERT INTO `mensaje`(`channel_id`,`id_afectado`, `message`) VALUES ('{message.channel.id}','{message.messages.content}', '{message.author.id}')")

client.run("Njc5Njg4NTgxMzM3NTc5NTc2.Gjoj9O.m9doRgjqVdjMzYpj7cn1r-ALPk9F_Bt3zHm-AQ")
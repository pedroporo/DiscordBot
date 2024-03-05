import discord
from discord import app_commands
from discord.ext import commands
class Testeos(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
    @app_commands.command(name="estension",description="Esto es un test")
    async def exten(self,interaction:discord.Interaction):
        await interaction.response.send_message("Hola Mundo!")
async def setup(bot:commands.Bot):
    await bot.add_cog(Testeos(bot))
        
def mirar():
    print("Hola que tal")


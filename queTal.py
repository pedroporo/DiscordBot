import os
import platform

class Testeo:
    async def load_cogs(self) -> None:
        """
        The code in this function is executed whenever the bot will start.
        """
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/fun"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"fun.{extension}")
                    self.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    self.logger.error(
                        f"Failed to load extension {extension}\n{exception}"
                    )
    

#for f in os.listdir('./cogs'):
#    if f.endswith('.py'):
#        bot.load_extension(f'cogs.{f[:-3]}')
import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    async def toggle():
        

async def setup(bot):
    await bot.add_cog(Misc(bot))

import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        bot.mod_channel = None

    @commands.command()
    async def ping(self, ctx):
        """Returns bot latency to client"""
        return await ctx.send(
            f"Pong! Latency: {self.bot.ws.latency * 1000:.4f}ms"
        )


async def setup(bot):
    await bot.add_cog(Commands(bot))

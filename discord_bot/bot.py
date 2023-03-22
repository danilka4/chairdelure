import os
from re import split

import discord
from discord.ext import commands
from dotenv import load_dotenv


class DiscordGPT(commands.Bot):
    def __init__(self):
        """Sets permissions and initializes bot object"""
        intents = discord.Intents.all()
        super().__init__(command_prefix="*", intents=intents)

    async def load_extensions(self):
        """Loads commands (called cogs or extensions)"""
        try:
            await self.load_extension("commands")
            print("Successfully loaded commands.")
        except Exception:
            print("Failed to load commands.")

    async def on_connect(self):
        await self.load_extensions()

    async def on_ready(self):
        """Bot startup"""
        print(f"{self.user.name} has connected to Discord!")

    async def on_command_error(self, ctx, error):
        """Sends error message if caught, else raise error to terminal"""
        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(
                f"Command not found: `{split(r'[ *]+', ctx.message.content)[1]}`"
            )
        raise error


def main():
    # Pulls bot token from environment 
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = DiscordGPT()
    # Spins up bot instance
    bot.run(TOKEN)


if __name__ == "__main__":
    main()

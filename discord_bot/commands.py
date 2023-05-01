from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Returns bot latency to client"""
        return await ctx.send(
            f"Pong! Latency: {self.bot.ws.latency * 1000:.4f}ms"
        )

    @commands.command()
    async def markov(self, ctx, *args):
        """Returns output from markov model based on user input"""
        if 1 > len(args) > 2:
            return await ctx.send("Input must be 1-2 words.")
        try:
            output = self.bot.markov_model.make_sentence_with_start(
                " ".join(args), max_chars=180
            )
            return await ctx.send(output)
        except Exception as e:
            if str(e).split()[-1] == " ".join(args):
                return await ctx.send(
                    f"Model did not return an output with start words `{' '.join(args)}`"
                )
            return await ctx.send(
                f"Model returned an invalid run with start words `{' '.join(args)}`"
            )


async def setup(bot):
    await bot.add_cog(Commands(bot))

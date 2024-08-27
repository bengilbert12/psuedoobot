from twitchio.ext import commands


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")


def prepare(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))

from twitchio.ext import commands

from utils.db import Database, TinyDatabase


class CustomCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = Database(provider=TinyDatabase("db.json"))

    @commands.command(aliases=["addcmd"])
    async def add_command(self, ctx, label: str, response: str):
        self.db.add_custom_command(
            streamer=ctx.channel.name, label=label, response=response
        )
        await ctx.send("New command added, maybe.")

    @commands.command(aliases=["rmcmd"])
    async def remove_command(self, ctx, label: str):
        self.db.remove_custom_command(streamer=ctx.channel.name, label=label)
        await ctx.send("Command removed, maybe.")


def prepare(bot: commands.Bot):
    bot.add_cog(CustomCommandCog(bot))

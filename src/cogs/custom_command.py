from twitchio.ext import commands

from utils.db import add_custom_command, remove_custom_command


class CustomCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["addcmd"])
    async def add_command(self, ctx, label: str, response: str):
        add_custom_command(streamer=ctx.channel.name, label=label, response=response)
        await ctx.send("New command added, maybe.")

    @commands.command(aliases=["rmcmd"])
    async def remove_command(self, ctx, label: str):
        remove_custom_command(streamer=ctx.channel.name, label=label)
        await ctx.send("Command removed, maybe.")


def prepare(bot: commands.Bot):
    bot.add_cog(CustomCommandCog(bot))

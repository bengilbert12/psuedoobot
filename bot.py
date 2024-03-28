import os

from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PREFIX = os.getenv("PREFIX", "?")


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=ACCESS_TOKEN,
            prefix=PREFIX,
            initial_channels=["psuedoo"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message):
        if message.echo:
            return
        print(f"{message.author.name}: {message.content}")

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("Join our discord server at https://discord.gg/UcFgW6A")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")


bot = Bot()
bot.run()

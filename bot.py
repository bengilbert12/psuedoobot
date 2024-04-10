import os

from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "None")
PREFIX = os.getenv("PREFIX", "?")
SOCIAL_LINKS = {
    "Discord": "https://discord.gg/UcFgW6A",
    "Instagram": "https://www.instagram.com/psuedoo_ttv/",
}


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
        await ctx.send(f"Join our discord server at {SOCIAL_LINKS['Discord']}")

    @commands.command(aliases=["insta", "ig"])
    async def instagram(self, ctx: commands.Context):
        await ctx.send(f"Come follow on instagram here: {SOCIAL_LINKS['Instagram']}")

    @commands.command()
    async def socials(self, ctx: commands.Context):
        social_message = ""
        for name, link in SOCIAL_LINKS.items():
            social_message += f"{name} | {link} | "

        await ctx.send(social_message)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")


bot = Bot()
bot.run()

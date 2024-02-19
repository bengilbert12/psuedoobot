import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix="!", initial_channels=["psuedoo"])

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


bot = Bot()
bot.run()

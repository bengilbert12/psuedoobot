import os

from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "None")
PREFIX = os.getenv("PREFIX", "?")


initial_cogs = [
    "cogs.basic",
    "cogs.psuedoo",
]


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=ACCESS_TOKEN,
            prefix=PREFIX,
            initial_channels=[
                "psuedoo",
            ],
        )

        for cog in initial_cogs:
            try:
                self.load_module(cog)
            except Exception as e:
                print(f"Failed to load cog {cog}.", e)

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message):
        if message.echo:
            return
        print(f"{message.author.name}: {message.content}")

        await self.handle_commands(message)


bot = Bot()
bot.run()

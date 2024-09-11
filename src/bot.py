import os

from dotenv import load_dotenv
from twitchio.ext import commands

from utils.db import Database, TinyDatabase

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "None")
PREFIX = os.getenv("PREFIX", "?")


initial_cogs = [
    "cogs.basic",
    "cogs.psuedoo",
    "cogs.custom_command",
]


class Bot(commands.Bot):

    def __init__(self):
        streamers = ["psuedoo"]
        super().__init__(
            token=ACCESS_TOKEN,
            prefix=PREFIX,
            initial_channels=streamers,
        )

        self.db = Database(provider=TinyDatabase(filename="db.json"))
        self.db.populate_streamers(streamers)

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

        streamer = message.channel.name

        try:
            custom_command_label = message.content.split(PREFIX)[1]

            if not self.db.custom_command_exists(streamer, custom_command_label):
                await self.handle_commands(message)
                return

            response = self.db.get_custom_command_response(
                streamer=streamer, label=custom_command_label
            )

            if not response:
                await self.handle_commands(message)
                return

            await message.channel.send(response)
        except IndexError:
            # Normal message
            await self.handle_commands(message)
            return


bot = Bot()
bot.run()

import os

import twitchio
from dotenv import load_dotenv
from twitchio.ext import commands, pubsub

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

client = twitchio.Client(token=ACCESS_TOKEN)
client.pubsub = pubsub.PubSubPool(client)


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix="!", initial_channels=["psuedoo"])
        self.sub = pubsub.PubSubPool(self)

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


@client.event()
async def event_pub_sub_channel_points(event):
    event.channel.send("Something happened")


# TODO: Add the async def main() at the bottom of https://twitchio.dev/en/stable/exts/pubsub.html#a-quick-example

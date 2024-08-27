from twitchio.ext import commands


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.social_links = {
            "Discord": "https://discord.gg/UcFgW6A",
            "Instagram": "https://www.instagram.com/psuedoo_ttv/",
            "Youtube": "https://youtube.com/@psuedoo",
        }

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"Join our discord server at {SOCIAL_LINKS['Discord']}")

    @commands.command(aliases=["insta", "ig"])
    async def instagram(self, ctx: commands.Context):
        await ctx.send(f"Come follow on instagram here: {SOCIAL_LINKS['Instagram']}")

    @commands.command(aliases=["yt"])
    async def youtube(self, ctx: commands.Context):
        await ctx.send(f"Sub to me on youtube! {SOCIAL_LINKS['Youtube']}")

    @commands.command()
    async def socials(self, ctx: commands.Context):
        social_message = ""
        for name, link in SOCIAL_LINKS.items():
            social_message += f"{name} | {link} | "

        await ctx.send(social_message)

    @commands.command(aliases=["pom"])
    async def pomodoro(self, ctx):
        await ctx.send(
            "We are using a Pomodoro Technique for time management. Psuedoo is not reading chat during the work time. He will readover chat during a break. Read more about the technique here: https://en.wikipedia.org/wiki/Pomodoro_Technique"
        )


def prepare(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))

from discord.ext import commands
from utils.utils import admin_role


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='hello_world', help='<extra_text>')
    @commands.has_role(admin_role)
    @commands.guild_only()
    async def hello_world(self, ctx, extra_text: str):
        await ctx.send("Hello World! " + extra_text)

def setup(bot):
    bot.add_cog(Hive(bot))

from discord.ext import commands

from utils.utils import admin_role


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='$NAME', help='')
    @commands.has_role(admin_role)
    @commands.guild_only()
    async def $NAME(self, ctx):

    pass


def setup(bot):
    bot.add_cog(Hive(bot))

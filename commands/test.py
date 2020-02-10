from discord.ext import commands

from utils.utils import admin_role


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='test', help='test command')
    @commands.has_role('Hive Master')
    @commands.guild_only()
    async def test(self, ctx, member):
        member = str(member)
        memberConverter = commands.MemberConverter()
        member = await memberConverter.convert(ctx, member)
        await ctx.send('```{}```'.format(member))


def setup(bot):
    bot.add_cog(Hive(bot))

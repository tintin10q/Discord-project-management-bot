import random

from discord.ext import commands


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='roll_dice',
                      help='<min> <max>')
    async def roll_dice(self, ctx, min: int, max: int):
        await ctx.send(random.randint(min, max))


def setup(bot):
    bot.add_cog(Hive(bot))

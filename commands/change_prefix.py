from discord.ext import commands

from databases.database_manager import db
from utils.utils import admin_role, get_bot_config


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='change_prefix', help='<prefix>')
    @commands.has_role(admin_role)
    async def change_prefix(self, ctx, new_prefix):
        bot_config = get_bot_config()
        bot_config["command_prefix"] = new_prefix
        db.set("bot_config", bot_config)
        self.bot.command_prefix = new_prefix
        await ctx.message.add_reaction('✅')


def setup(bot):
    bot.add_cog(Hive(bot))

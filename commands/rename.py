from discord.ext import commands

from databases.database_manager import db
from utils.utils import get_command_prefix, admin_role


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='rename',
                      help='| {}rename <old_map_name> <new_map_name>'.format(
                          get_command_prefix()))
    @commands.has_role(admin_role)
    async def add_map(self, ctx, old_name, new_name):
        old_name = old_name.title()
        new_name = new_name.title()
        map_id = db.translate(old_name)

        if map_id is None:
            await ctx.send("Sorry, I could not find `{}` in the database 🙁".format(old_name))
            return
        else:
            # change in the translation file the map file and the channel name on the discord

            # Maps
            maps = db.get("maps")
            maps[map_id]["name"] = new_name
            db.set("maps", maps)

            # Translation
            translations = db.get("translations")
            translations[new_name] = translations.pop(old_name)
            db.set("translations", translations)

            # Channel in discord
            await ctx.guild.get_channel(maps[map_id]["category_id"]).edit(name=new_name)
            await ctx.message.add_reaction('✅')


def setup(bot):
    bot.add_cog(Hive(bot))

from discord.ext import commands

from databases.database_manager import db


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='get_map_id', help='<map_name>',aliases=["get_id","gmi"])
    async def get_map_id(self, ctx, map_name):
        map_name = map_name.title()
        map_id = db.translate(map_name)
        if map_id is None:
            await ctx.send("Sorry, I could not find `{}` in the database 🙁".format(map_name))
            return
        else:
            await ctx.send("The id for the `{}` map is `{}`".format(map_name, map_id))


def setup(bot):
    bot.add_cog(Hive(bot))

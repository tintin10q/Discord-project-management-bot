from discord.ext import commands

from databases.database_manager import db
from utils.utils import map_role_pattern


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='signed_up_maps',
                      help='<member_name>',
                      aliases=["sup"])
    @commands.guild_only()
    async def signed_up_maps(self, ctx, member):
        memberConverter = commands.MemberConverter()
        member = await memberConverter.convert(ctx, member)
        map_roles = []
        for role in member.roles:
            if map_role_pattern.match(role.name):
                map_roles.append(role)
        output_string = "-= {} =-\n".format(member.nick)
        for role in map_roles:
            map_name = db.translate(role.name)
            output_string += "● {}\n".format(map_name)
        await ctx.send(output_string)


def setup(bot):
    bot.add_cog(Hive(bot))

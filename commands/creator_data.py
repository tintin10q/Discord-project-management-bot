import re

from discord.ext import commands

from databases.database_manager import db
from utils.utils import get_command_prefix


class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='emp_data',
                      help='| {}emp_data <emp_name>'.format(get_command_prefix()))
    async def show_intrested(self, ctx, emp_name=None):
        map_name = map_name.title()
        if map_name in ("All", "*"):
            roles = ctx.guild.roles
            pattern = re.compile('[A-Z]+-[0-9]+')
            interested_roles = []
            for role in roles:
                if pattern.match(role.name):
                    interested_roles.append(role)
            output_string = "Here are all the maps with the interested people:\n"
            for role in interested_roles:
                output_string += '`-= {} =-`\n'.format(db.get("maps")[role.name]["name"])
                for member in role.members:
                    output_string += '{}\n'.format(member.nick)
                output_string += "\n"
            await ctx.send(output_string)
        else:
            map_id = db.translate(map_name)
            if map_id is None:
                await ctx.send("Sorry, I could not find `{}` in the database 🙁".format(map_name))
                return
            interested_list = []
            role_id = db.get("maps")[map_id]["role_id"]
            for member in ctx.guild.members:
                if ctx.guild.get_role(role_id) in member.roles:
                    interested_list.append(member.nick)
            # Quite ugly way to patch sting together
            # intrested_list.sort()
            message_string = """`-= {} =-`\n""".format(map_name)
            for name in interested_list:
                message_string += "{}\n".format(name)
            # message_string += "```"
            await ctx.send(message_string)

        for member in ctx.guild.members:
            if member.nick == emp_name:
                target_member = member
                break
        for role in target_member.roles:
            


def setup(bot):
    bot.add_cog(Hive(bot))

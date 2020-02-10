import discord
from discord.ext import commands

from databases.database_manager import db
from utils.utils import get_command_prefix, admin_role, archive_name


class Hive(commands.Cog):

    @commands.command(name='archive_map',
                      help='<map_name>',)
    @commands.has_role('Hive Master')
    @commands.guild_only()
    async def archive_map(self, ctx, map_name):
        map_name = map_name.title()
        map_id = db.translate(map_name)
        if map_id is None:
            await ctx.send("Sorry, I could not find `{}` in the database 🙁".format(map_name))
            return
        else:
            # Detect/Make the archived channel
            archive_channel = discord.utils.get(ctx.guild.channels, name=archive_name)
            if archive_channel is None:
                await ctx.guild.create_category(name=archive_name)
                archive_channel = discord.utils.get(ctx.guild.channels, name=archive_name)

            # Get the data
            maps = db.get("maps")
            map_info = maps[map_id]
            map_name = map_info["name"]
            map_id = map_info["id"]
            # Do things with the data
            await ctx.guild.get_role(map_info["role_id_mute"]).delete()
            await ctx.guild.get_role(map_info["role_id"]).delete()
            await ctx.guild.get_channel(map_info["project_info_channel_id"]).edit(category=archive_channel,
                                                                                  name="{}-dissusion".format(map_name))
            await ctx.guild.get_channel(map_info["discussion_channel_id"]).edit(category=archive_channel,
                                                                                name="{}-discussion".format(map_name))
            await ctx.guild.get_channel(map_info["category_id"]).delete()
            archive_channel = discord.utils.get(ctx.guild.channels, name=archive_name)
            # Remove the map from the maps database
            maps.pop(map_id)
            db.set("maps", maps)
            await ctx.message.add_reaction('✅')
        return


def setup(bot):
    bot.add_cog(Hive(bot))

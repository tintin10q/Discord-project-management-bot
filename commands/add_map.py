import discord
from discord.ext import commands
from utils.utils import get_command_prefix, admin_role, get_map_types, get_bot_config, generate_map_id
from databases.database_manager import db

class Hive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='add_map',
                 help='| {}add_map <map_type> <map_name>'.format(get_command_prefix()))
    @commands.has_role(admin_role)
    async def add_map(self, ctx, map_type, map_name):
        map_type = map_type.lower()
        map_name = map_name.title()
        if map_name in db.get("translations"):
            await ctx.send("This map name is already taken")
            return

        if map_type not in get_map_types():  # Check if map type given is registered
            await ctx.send("Please only have: `{}` as maptype".format(get_map_types()))
            return

        bot_config = get_bot_config()

        if map_type in bot_config["map_types"]:  # If the map type is registered and long turn it short
            map_type = bot_config["map_types"][map_type]

        map_id = generate_map_id(bot_config, map_type)  # Generate the id
        role_names = (map_id, ("!{}".format(map_id)))
        # await ctx.send("{}".format(map_id))

        new_roles = []  # Add the new roles
        for role_name in role_names:
            new_roles.append(
                await ctx.guild.create_role(reason="Added '{}' for the new map called '{}'".format(role_name, map_name),
                                            name=role_name,
                                            color=discord.Color.dark_grey(),
                                            hoist=False,
                                            mentionable=False))

        # Add the permissions for the category
        non_read = discord.PermissionOverwrite(read_messages=False)
        read = discord.PermissionOverwrite(read_messages=True)

        category_permissions = {
            ctx.guild.default_role: read,
            new_roles[1]: non_read,
            new_roles[0]: read

        }  # New roles is and should alwyas be like [read_role,non_read_role]

        # Add the category
        new_category = await ctx.guild.create_category(name=map_name,
                                                       overwrites=category_permissions,
                                                       reason="Made the catogory for the new '{}' map".format(map_name))

        # Add the 2 channels to the category
        dissucion_channel = await ctx.guild.create_text_channel(name="project-info",
                                                                category=new_category,
                                                                topic="The project info for {}".format(map_name))
        project_info_channel = await ctx.guild.create_text_channel(name="discussion",
                                                                   category=new_category,
                                                                   topic="The discussion channel for {}".format(
                                                                       map_name))
        # Write map data to database
        new_map_data = {
            "name": map_name,
            "id": map_id,
            "discussion_channel_id": dissucion_channel.id,
            "project_info_channel_id": project_info_channel.id,
            "role_id": new_roles[0].id,
            "role_id_mute": new_roles[1].id,
            "category_id": new_category.id
        }
        maps = db.get("maps")
        maps[map_id] = new_map_data
        db.set("maps", maps)

        # Write translation data to database
        translations = db.get("translations")
        translations[map_name] = map_id
        db.set("translations", translations)
        await ctx.message.add_reaction('✅')
        await ctx.send('The Role names are: `{}` and `{}`'.format(map_id, '!' + map_id), delete_after=600)

def setup(bot):
    bot.add_cog(Hive(bot))
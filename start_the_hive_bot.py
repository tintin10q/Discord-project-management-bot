# bot.py

import re
import discord
from discord.ext import commands

from databases.database_manager import db
from utils.utils import get_bot_config, get_command_prefix

bot_config = get_bot_config()

token = db.get("bot_token")["token"]  # Have a file called bot_token.json with {"token":"token here"}
bot = commands.Bot(command_prefix=get_command_prefix())

bot.load_extension("commands.add_map")
bot.load_extension("commands.archive_map")
bot.load_extension("commands.change_prefix")
bot.load_extension("commands.get_map_id")
bot.load_extension("commands.rename")
bot.load_extension("commands.roll_dice")
bot.load_extension("commands.show_intrest")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    if isinstance(error, discord.errors.HTTPException):
        await ctx.send('Something went wrong with the connection')
    await ctx.send('```Error: {}```'.format(error))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(token)

# bot.py

import discord
from discord.ext import commands

from databases.database_manager import db
from utils.utils import get_bot_config, get_command_prefix

bot_config = get_bot_config()

token = db.get("bot_token")
if token is None:
    print('''
NO TOKEN FOUND!
Please add the bot token in: 'databases/bot_token.json' with:
    
{"token": "Your token here"}''')
    exit()

token = token["token"]  # Have a file called bot_token.json with {"token":"token here"}
bot = commands.Bot(command_prefix=get_command_prefix())

# bot.load_extension("commands.test")

bot.load_extension("commands.add_map")
bot.load_extension("commands.archive_map")
bot.load_extension("commands.change_prefix")
bot.load_extension("commands.get_map_id")
bot.load_extension("commands.rename")
bot.load_extension("commands.roll_dice")
bot.load_extension("commands.show_interest")
bot.load_extension("commands.signed_up_maps")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    elif isinstance(error, discord.errors.HTTPException):
        await ctx.send('Something went wrong with the connection')
    elif isinstance(error, discord.ext.commands.CommandNotFound):
        return
    else:
        await ctx.send('{}'.format(error))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='ping')
async def add_map(ctx):
    await ctx.message.add_reaction('✅')


bot.run(token)

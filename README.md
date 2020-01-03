# Discord-project-management-bot
This bot can keep track of pitches and make channels for them

# Setup
To start using the bot make sure that you have installed the discord package with:

`pip3 install discord`

Then add your bot token in databases/bot_token.json with:

`{"token":"Your bot token"}`

# Help command 
```
This is the command list (might be not up to date)
Hive:
  add_map       | -add_map <map_type> <map_name>------------- Adds a project to the server
  archive_map   | -archive_map <map_name>-------------------- Moves a project to archived
  change_prefix | -change_prefix <prefix>-------------------- Change the bot prefix
  get_map_id    | -get_map_id <map_name>--------------------- Get the id for a map
  rename        | -rename <old_map_name> <new_map_name>------ Rename a map
  roll_dice     | -roll_dice <min> <max>--------------------- Roll a dice
  show_interest  | -show_intrest <map_name> or <all/*>-------- See who is intrested in a map
​No Category:
  help          Shows this message
Type -help command for more info on a command.
You can also type -help category for more info on a category.
```

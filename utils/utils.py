

from databases.database_manager import db


def generate_map_id(bot_config, map_type):
    """ This function generates a new id for a map and adds to the id counter"""
    map_id = bot_config["map_ids"][map_type]  # Get the newest id in the database
    map_id = str(map_id)

    while len(map_id) < 4:
        map_id = "0{}".format(map_id)
    map_id_final = '{map_type}-{map_id}'.format(map_type=map_type, map_id=map_id)

    bot_config["map_ids"][map_type] += 1
    db.set("bot_config", bot_config)

    return map_id_final.upper()


def get_map_types():
    """ This function exist to get a list of all the map id's registered.
        This way the bot does not have to be restart                        """
    bot_config = db.get("bot_config")
    map_types_list = []
    for i in bot_config["map_types"].items():
        map_types_list.extend([i[0], i[1]])
    return map_types_list

def get_bot_config():
    return db.get("bot_config")

def get_command_prefix():
    return db.get("bot_config")["command_prefix"]

admin_role = get_bot_config()["admin_role_name"]
archive_name = get_bot_config()["archived_channel_name"]
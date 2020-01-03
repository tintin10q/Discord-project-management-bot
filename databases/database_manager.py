import json
import os


class Database():
    """"A simple class to manage a json database made by Quinten Cabo"""
    my_path = os.path.dirname(os.path.realpath(__file__))

    def get(self, name):
        """Will return a database with the name given. So get(users) with get users.json"""
        try:
            database_path = os.path.join(os.path.dirname(__file__), name + ".json")
            database_file = open(database_path, "r+")
            database = json.load(database_file)
        except FileNotFoundError:
            print("Could not find {}.json".format(name))
            return None
        return database

    def set(self, name, data):
        """Will set a database with the name given. So set(users,data) with set users.json with data"""
        database_path = os.path.join(os.path.dirname(__file__), name + ".json")
        json.dump(data, open(database_path, "w+"), indent=4, sort_keys=True)

    def insert(self, name, data):
        """ Will append data to a list named <name> in a file named <name>.json
        database = self.get(name)
        database[name].append(data)
        self.set(name,database)"""
        self.set(name, self.get(name)[name].append(data))

    def reset(self):
        """Will reset all databases. They should be registered manually"""
        self.set("players", {})
        self.set("uuid_list", {"uuid_list": []})
        self.set("gamedata", {"player_count": 0, "death_score": -1})
        return

    def translate(self, name, file_name="translations"):
        """ Will translate a name to the corresponding ID """
        translations = self.get(file_name)
        if name in translations:
            return translations[name]
        else:
            return None


db = Database()

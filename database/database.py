import json
import os


DB_FILE = "noorsepiens.json"



default_data = {
    "users": [],
    "memory": [],
    "long_memory": []
}



def load_db():

    if not os.path.exists(DB_FILE):

        save_db(default_data)

        return default_data


    with open(DB_FILE, "r") as file:

        return json.load(file)




def save_db(data):

    with open(DB_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

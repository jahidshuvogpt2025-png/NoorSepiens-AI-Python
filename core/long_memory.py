import json
import os



FILE = "long_memory.json"




DEFAULT_MEMORY = {

    "identity": {},

    "preferences": {},

    "skills": {},

    "goals": {},

    "facts": {}

}





def load_memory():

    if not os.path.exists(FILE):

        save_memory(DEFAULT_MEMORY)

        return DEFAULT_MEMORY


    with open(FILE, "r", encoding="utf-8") as f:

        return json.load(f)






def save_memory(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )







def add_memory(category, key, value):


    memory = load_memory()



    if category not in memory:

        memory[category] = {}



    memory[category][key] = value



    save_memory(memory)







def get_memory():

    return load_memory()







def clear_memory():

    save_memory(DEFAULT_MEMORY)

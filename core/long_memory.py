import json
import os



FILE = "long_memory.json"



def load_memory():

    if not os.path.exists(FILE):

        return {}


    with open(FILE,"r") as f:

        return json.load(f)




def save_memory(data):

    with open(FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )




def add_memory(key,value):

    memory = load_memory()


    memory[key] = value


    save_memory(memory)




def get_memory():

    return load_memory()

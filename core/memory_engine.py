import json
import os
from datetime import datetime


MEMORY_FILE = "core/long_memory.json"


DEFAULT_MEMORY = {

    "identity": {},

    "preferences": {},

    "skills": {},

    "goals": {},

    "facts": {},

    "history": []

}





def load_memory():

    if not os.path.exists(MEMORY_FILE):

        save_memory(DEFAULT_MEMORY)

        return DEFAULT_MEMORY


    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        return DEFAULT_MEMORY






def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )







class MemoryEngine:


    def __init__(self):

        self.memory = load_memory()





    def add(self, category, key, value):


        if category not in self.memory:

            self.memory[category] = {}



        self.memory[category][key] = value


        self.save()






    def remember_chat(self, user, bot):


        self.memory["history"].append({

            "user": user,

            "bot": bot,

            "time": str(datetime.now())

        })



        # keep last 50 chats

        self.memory["history"] = (
            self.memory["history"][-50:]
        )


        self.save()







    def get(self):

        return self.memory






    def save(self):

        save_memory(
            self.memory
        )







    def clear(self):

        self.memory = DEFAULT_MEMORY

        self.save()






memory = MemoryEngine()
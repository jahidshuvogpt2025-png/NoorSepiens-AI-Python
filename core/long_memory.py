import json
import os



# Permanent memory file location

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


FILE = os.path.join(
    BASE_DIR,
    "long_memory.json"
)





DEFAULT_MEMORY = {

    "identity": {},

    "preferences": {},

    "skills": {},

    "goals": {},

    "facts": {}

}





# ================= LOAD MEMORY =================


def load_memory():

    if not os.path.exists(FILE):

        save_memory(DEFAULT_MEMORY)

        return DEFAULT_MEMORY



    try:

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    except:

        return DEFAULT_MEMORY







# ================= SAVE MEMORY =================


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








# ================= ADD MEMORY =================


def add_memory(
    category,
    key,
    value
):


    memory = load_memory()



    if category not in memory:

        memory[category] = {}



    memory[category][key] = value



    save_memory(memory)







# ================= OLD SYSTEM SUPPORT =================


def saveLongMemory(
    chatId,
    key,
    value
):


    category = "facts"



    if key in [

        "name",
        "call",
        "nickname"

    ]:

        category = "identity"



    elif key in [

        "like",
        "dislike",
        "interest"

    ]:

        category = "preferences"



    elif key in [

        "skill"

    ]:

        category = "skills"



    elif key in [

        "goal"

    ]:

        category = "goals"





    add_memory(

        category,

        key,

        value

    )








# ================= GET MEMORY =================


def get_memory():

    return load_memory()







# ================= CLEAR MEMORY =================


def clear_memory():

    save_memory(
        DEFAULT_MEMORY
    )

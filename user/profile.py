from database.database import load_db, save_db
from datetime import datetime



def create_user(user_id, username="", name=""):

    db = load_db()


    exists = False


    for user in db["users"]:

        if user["id"] == str(user_id):

            exists = True



    if not exists:

        db["users"].append({

            "id": str(user_id),

            "username": username,

            "name": name,

            "created": str(datetime.now())

        })


        save_db(db)





def get_profile(user_id):

    db = load_db()


    for user in db["users"]:

        if user["id"] == str(user_id):

            return user


    return None

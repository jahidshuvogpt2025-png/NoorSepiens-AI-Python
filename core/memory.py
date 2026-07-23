from core.long_memory import add_memory, get_memory



class Memory:


    def save(self, key, value):

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





    def get(self):

        return get_memory()

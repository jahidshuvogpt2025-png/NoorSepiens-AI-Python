from ai.router import AIRouter
from core.memory import Memory
from core.long_memory import (
    add_memory,
    get_memory
)



class NoorAgent:


    def __init__(self):

        self.name = "NoorSepiens AI"

        self.ai = AIRouter()

        self.memory = Memory()



    def response(self, text):


        # Save conversation memory

        self.memory.save(text)



        # Auto save simple memories

        lower = text.lower()



        if "আমার নাম" in text:

            name = text.replace(
                "আমার নাম",
                ""
            ).strip()


            add_memory(
                "name",
                name
            )



        if "আমি" in text and "শিখছি" in text:

            skill = text.replace(
                "আমি",
                ""
            ).replace(
                "শিখছি",
                ""
            ).strip()


            add_memory(
                "skill",
                skill
            )



        if "আমার লক্ষ্য" in text:

            goal = text.replace(
                "আমার লক্ষ্য",
                ""
            ).strip()


            add_memory(
                "goal",
                goal
            )





        history = self.memory.get()



        long_memory = get_memory()



        prompt = f"""

You are NoorSepiens AI.

Reply in Bangla.


User Long Term Memory:

{long_memory}


Recent Conversation:

{history}


User:

{text}


Use memory naturally.

Be helpful and friendly.

"""



        reply = self.ai.ask(
            prompt
        )



        self.memory.save(
            "Assistant: " + reply
        )


        return reply

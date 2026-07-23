from ai.router import AIRouter
from core.memory import Memory



class NoorAgent:


    def __init__(self):

        self.name = "NoorSepiens AI"

        self.ai = AIRouter()

        self.memory = Memory()



    def response(self, text):


        # Save user message

        self.memory.save(text)



        history = self.memory.get()



        context = "\n".join(history)



        prompt = f"""

You are {self.name}.

Reply in Bangla.

Previous conversation:

{context}


Current user message:

{text}


Be helpful, friendly and intelligent.

"""



        reply = self.ai.ask(
            prompt
        )



        # Save AI reply

        self.memory.save(
            "Assistant: " + reply
        )



        return reply

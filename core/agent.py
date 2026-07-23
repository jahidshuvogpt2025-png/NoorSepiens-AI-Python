from ai.router import AIRouter



class NoorAgent:


    def __init__(self):

        self.name = "NoorSepiens AI"

        self.ai = AIRouter()



    def response(self, text):


        prompt = f"""
You are {self.name}.

Reply in Bangla.

User message:

{text}

Be helpful, friendly and intelligent.
"""


        reply = self.ai.ask(
            prompt
        )


        return reply

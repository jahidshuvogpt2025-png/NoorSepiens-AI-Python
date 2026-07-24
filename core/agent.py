import os
import requests

from core.memory_engine import memory




class NoorAgent:


    def __init__(self):

        self.api_key = os.getenv(
            "OPENROUTER_API_KEY"
        )

        self.model = "openai/gpt-4o-mini"






    def build_memory_context(self):


        data = memory.get()


        context = """

USER MEMORY:

"""



        for category, values in data.items():


            if category == "history":

                continue



            if values:


                context += f"\n{category.upper()}:\n"



                for key, value in values.items():

                    context += (
                        f"{key}: {value}\n"
                    )



        return context







    def response(self, text):


        memory_context = self.build_memory_context()



        prompt = f"""

You are NoorSepiens AI.

You are a personal AI assistant.


User permanent memory:

{memory_context}



Rules:

- Always use memory when answering.
- If user asks about himself, use saved identity.
- Respect user's preferred name.
- Reply in Bangla.
- Never invent user information.
- Be natural and friendly.



User message:

{text}

"""



        try:


            response = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers={

                    "Authorization":
                    f"Bearer {self.api_key}",

                    "Content-Type":
                    "application/json"

                },


                json={

                    "model": self.model,

                    "messages":[

                        {

                            "role":"system",

                            "content":prompt

                        },

                        {

                            "role":"user",

                            "content":text

                        }

                    ]

                },

                timeout=60

            )



            result = response.json()



            reply = (
                result["choices"][0]
                ["message"]
                ["content"]
            )



            # save conversation

            memory.remember_chat(

                text,

                reply

            )



            return reply




        except Exception as e:


            print(
                "AI ERROR:",
                e
            )


            return "AI response error ❌"
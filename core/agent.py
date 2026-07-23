import os
import requests

from core.long_memory import get_memory



class NoorAgent:


    def __init__(self):

        self.api_key = os.getenv(
            "OPENROUTER_API_KEY"
        )

        self.model = "openai/gpt-4o-mini"





    def build_context(self):


        memory = get_memory()


        context = ""


        if memory.get("identity"):

            context += (
                "User Identity:\n"
            )

            for k,v in memory["identity"].items():

                context += f"{k}: {v}\n"




        if memory.get("preferences"):

            context += (
                "\nUser Preferences:\n"
            )

            for k,v in memory["preferences"].items():

                context += f"{k}: {v}\n"




        if memory.get("skills"):

            context += (
                "\nUser Skills:\n"
            )

            for k,v in memory["skills"].items():

                context += f"{k}: {v}\n"




        if memory.get("goals"):

            context += (
                "\nUser Goals:\n"
            )

            for k,v in memory["goals"].items():

                context += f"{k}: {v}\n"



        return context







    def response(self, text):


        memory_context = self.build_context()



        prompt = f"""

You are NoorSepiens AI.

Important user memory:
{memory_context}


Rules:
- Always respect saved memory.
- Call user according to identity preference.
- Never invent personal information.
- Answer naturally in Bangla.


User:
{text}

"""



        try:


            result = requests.post(

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
                        }

                    ]

                }

            )



            data = result.json()


            return data["choices"][0]["message"]["content"]



        except Exception as e:


            print(e)

            return "AI response error ❌"

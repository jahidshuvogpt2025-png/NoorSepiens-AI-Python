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



        identity = memory.get(
            "identity",
            {}
        )


        if identity:

            context += "\nUser Identity:\n"

            for k, v in identity.items():

                context += f"- {k}: {v}\n"




        preferences = memory.get(
            "preferences",
            {}
        )


        if preferences:

            context += "\nUser Preferences:\n"

            for k, v in preferences.items():

                context += f"- {k}: {v}\n"




        skills = memory.get(
            "skills",
            {}
        )


        if skills:

            context += "\nUser Skills:\n"

            for k, v in skills.items():

                context += f"- {k}: {v}\n"




        goals = memory.get(
            "goals",
            {}
        )


        if goals:

            context += "\nUser Goals:\n"

            for k, v in goals.items():

                context += f"- {k}: {v}\n"




        facts = memory.get(
            "facts",
            {}
        )


        if facts:

            context += "\nUser Facts:\n"

            for k, v in facts.items():

                context += f"- {k}: {v}\n"



        return context







    def response(self, text):


        memory = self.build_context()



        prompt = f"""

You are NoorSepiens AI.

You have a permanent memory system.

Saved user memory:

{memory}



Rules:

1. Always use saved memory when answering.
2. If user asks "আমি কে" or similar, answer from identity memory.
3. If user has a call name, use that name.
4. Never say you don't know if memory contains the answer.
5. Reply naturally in Bangla.
6. Be friendly and helpful.



User message:

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

                },

                timeout=60

            )



            data = result.json()


            return data["choices"][0]["message"]["content"]



        except Exception as e:


            print(e)


            return "AI response error ❌"
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


        context = """
USER LONG TERM MEMORY:

"""


        identity = memory.get("identity", {})


        if identity:

            context += "\nIdentity:\n"

            for key, value in identity.items():

                context += f"- {key}: {value}\n"




        preferences = memory.get(
            "preferences",
            {}
        )


        if preferences:

            context += "\nPreferences:\n"

            for key, value in preferences.items():

                context += f"- {key}: {value}\n"




        skills = memory.get(
            "skills",
            {}
        )


        if skills:

            context += "\nSkills:\n"

            for key, value in skills.items():

                context += f"- {key}: {value}\n"




        goals = memory.get(
            "goals",
            {}
        )


        if goals:

            context += "\nGoals:\n"

            for key, value in goals.items():

                context += f"- {key}: {value}\n"




        facts = memory.get(
            "facts",
            {}
        )


        if facts:

            context += "\nFacts:\n"

            for key, value in facts.items():

                context += f"- {key}: {value}\n"



        return context







    def response(self, text):


        memory_context = self.build_context()



        prompt = f"""

You are NoorSepiens AI.

You have permanent memory about the user.

{memory_context}


Memory rules:

- If identity name exists, it is the user's real name.
- If identity call exists, use that nickname when talking to the user.
- If user asks "আমার নাম কি" answer from memory.
- Do not ask again for information already stored.
- Always reply in natural Bangla.


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

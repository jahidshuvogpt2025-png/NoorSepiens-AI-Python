import os
import requests
from dotenv import load_dotenv


load_dotenv()



class AIRouter:


    def __init__(self):

        self.api_key = os.getenv(
            "OPENROUTER_API_KEY"
        )



    def ask(self, message):


        url = "https://openrouter.ai/api/v1/chat/completions"



        headers = {

            "Authorization":
            f"Bearer {self.api_key}",

            "Content-Type":
            "application/json"

        }



        data = {

            "model":
            "openai/gpt-4o-mini",


            "messages":[

                {

                    "role":"user",

                    "content":message

                }

            ]

        }



        response = requests.post(

            url,

            headers=headers,

            json=data

        )



        result = response.json()



        return result["choices"][0]["message"]["content"]

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY");


def ask_chatGPT(prompt, traits, user_message):


    personality_description = "\n".join([f"- {k}: {v}" for k, v in traits.item()])
    full_prompt = f"{prompt}\n{personality_description}"


    messages = [
        {"role": "system", "content" : prompt},
        {"role": "user", "content": user_message}
    ]


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
    )

    


    return response['choices'][0]['messages']['content']

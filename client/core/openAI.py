import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_chatGPT(prompt, traits, user_message):



    full_prompt = "\n".join(prompt + [f"- {trait}" for trait in traits])


    messages = [
        {"role": "system", "content" : full_prompt},
        {"role": "user", "content": user_message}
    ]


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
    )

    


    return response['choices'][0]['message']['content']

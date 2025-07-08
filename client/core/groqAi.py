from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


client = Groq(

    api_key=os.environ.get("GROQ_API_KEY"),

)

def ask_chatGROQ(prompt, traits, user_message):
    full_prompt = "\n".join([prompt] + [f"- {trait}" for trait in traits])

    messages = [
        {"role": "system", "content": full_prompt},
        {"role": "user", "content": user_message}
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192",  
    )

    return chat_completion.choices[0].message.content

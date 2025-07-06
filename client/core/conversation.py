import asyncio
from furhat_remote_api import FurhatRemoteAPI
from .openAI import ask_chatGPT
from .speech_to_text import *
import sys

def run_conversation(furhat, prompt, traits):
    furhat.say(text="Di che cosa vuoi parlare?")
    while True:
        user_utterance = transcribe_audio()

        if user_utterance.strip().lower() == "arrivederci":
            furhat.say(text="Arrivederci! A presto!")
            sys.exit(0)

        # Just for test
        print(f"Utente ha detto: {user_utterance}")

        response = ask_chatGPT(prompt, traits, user_utterance)
        furhat.say(text=response)



if __name__ == "__main__":
    furhat = FurhatRemoteAPI("")  
    prompt = "Sei un assistente virtuale gentile e disponibile."
    traits = "Estroverso"

    asyncio.run(run_conversation(furhat, prompt, traits))

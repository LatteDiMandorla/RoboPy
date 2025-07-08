import asyncio
import time
from furhat_remote_api import FurhatRemoteAPI
from .openAI import ask_chatGPT
from .speech_to_text import *
import sys

def run_conversation(furhat, prompt, traits):
    furhat.say(text="Di che cosa vuoi parlare?")
    time.sleep(6 * 0.4)
    while True:
        user_utterance = transcribe_audio_whisper()
        
        if user_utterance == "":
            continue

        if user_utterance.strip().lower() == "arrivederci":
            furhat.say(text="Arrivederci! A presto!")
            sys.exit(0)



        # Just for test
        print(f"Utente ha detto: {user_utterance}")

        response = ask_chatGPT(prompt, traits, user_utterance)
        furhat.say(text=response)

        # Pause the function based on the estimated speaking time
        time.sleep(len(response.split()) * 0.4)



if __name__ == "__main__":
    furhat = FurhatRemoteAPI("localhost")  
    prompt = "Sei un assistente virtuale gentile e disponibile."
    traits = "Estroverso"

    run_conversation(furhat, prompt, traits)

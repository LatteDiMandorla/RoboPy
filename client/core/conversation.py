import asyncio
from furhat_remote_api import FurhatRemoteAPI
from openAI import ask_chatGPT

async def run_conversation(furhat, prompt, traits):
    while True:
        user_utterance = await furhat.listen()

        if user_utterance.strip().lower() == "arrivederci":
            await furhat.say("Arrivederci! A presto!")
            break
        print(f"Utente ha detto: {user_utterance}")

        response = ask_chatGPT(prompt, traits, user_utterance)
        await furhat.say(response)



if __name__ == "__main__":
    furhat = FurhatRemoteAPI("")  
    prompt = "Sei un assistente virtuale gentile e disponibile."
    traits = {"extrovert": True}

    asyncio.run(run_conversation(furhat, prompt, traits))

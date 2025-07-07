from furhat_remote_api import FurhatRemoteAPI
import asyncio
from .speech_to_text import *
import sys
import time


parole_numeri = {
    "uno": 1, "due": 2, "tre": 3, "quattro": 4,
    "cinque": 5, "sei": 6, "sette": 7
}


def LaunchFurhatRobot():
    furhat = FurhatRemoteAPI("localhost")
    furhat.set_voice(name='Adriano-Neural')
    furhat.say(text="Ciao, sono RoboPAI. Posso porti qualche semplice domanda per conoscerci meglio?")
    
    time.sleep(11 * 0.4)
    while True:
        answer = transcribe_audio()

        if answer.strip().lower() == "":
            continue

        if answer.strip().lower() == "sì":
            risposte = chiedi_risposte(furhat)
            return furhat, risposte

        if answer.strip().lower() == "no":
            furhat.say(text="Va bene, torna quando sarai pronto!")
            sys.exit(0)


def chiedi_risposte(furhat):
    domande = [
        "1. Ti consideri estroverso?",
        "2. Ti consideri critico, polemico?",
        "3. Ti consideri affidabile?",
        "4. Ti consideri ansioso?",
        "5. Sei aperto a nuove esperienze?",
        "6. Ti consideri riservato?",
        "7. Ti consideri simpatico?",
        "8. Ti consideri disorganizzato?",
        "9. Ti consideri calmo?",
        "10. Ti consideri poco creativo?"
    ]

    risposte = []
    furhat.say(text="Perfetto, ti propongo una serie di domande, dovrai rispondere fornendo un numero compreso tra 2 e 7.")
    time.sleep(17 * 0.4)
    for domanda in domande:
        furhat.say(text=domanda)

        while True:
            risposta = transcribe_audio().strip().lower()
            print(f"Risposta trascritta: '{risposta}'")  

            if risposta.strip().lower == "":
                continue

            try:
                if risposta in parole_numeri:
                    numero = parole_numeri[risposta]
                else:
                    numero = int(risposta)

                if 2 <= numero <= 7:
                    risposte.append(numero)
                    break
                else:
                    furhat.say(text="La risposta deve essere un numero da due a sette.")
            except ValueError:
                furhat.say(text="Non ho capito. Puoi dirmi un numero valido?")
                time.sleep(8 * 0.4)
    
    return risposte


async def look(furhat):
    
    try:
        while True:
            
            users = furhat.get_users()

            if users and len(users)>0:
                furhat.attend("CLOSEST")


            await asyncio.sleep(20)
    except Exception as e:
        print("ERRORE in look():", e)

    


#Define gesture based on personality 

#Extrovertion
extrovert = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"SMILE_OPEN": 1.0, "BROW_UP_LEFT": 0.7, "BROW_UP_RIGHT": 0.7}
        }
    ]
}

introvert = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"SMILE_CLOSED": 1.0, "BROW_DOWN_LEFT": 0.7, "BROW_DOWN_RIGHT": 0.7}
        }
    ]
}

friendly = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"LOOK_RIGHT": 0.3}
        }
    ]
}

unfriendly = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"LOOK_AWAY": 0.3}
        }
    ]
}

conscious = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"JAW_UP": 0.8}
        }
    ]
}

impulsive = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0], "params": {"JAW_DROP": 0.8, "EYE_SQUINT_RIGHT": 0.5}
        }
    ]
}

def handle_extrovert(gesture):
    furhat.gesture(body=extrovert)

def handle_introvert(gesture):
    furhat.gesture(body=introvert)

def handle_friendly(gesture):
    furhat.gesture(body=friendly)

def handle_unfriendly(gesture):
    furhat.gesture(body=unfriendly)

def handle_conscious(gesture):
    furhat.gesture(body=conscious)

def handle_impulsive(gesture):
    furhat.gesture(body=impulsive)



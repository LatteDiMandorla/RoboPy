from furhat_remote_api import FurhatRemoteAPI
import asyncio

def LaunchFurhatRobot():
    furhat = FurhatRemoteAPI("localhost")
    furhat.set_voice(name='Matthew')

    return furhat



async def look(furhat):
    try:
        while True:
            users = await asyncio.to_thread(lambda: furhat.get_users())
            print(f"Utenti rilevati: {users}")

            if users and len(users) > 0:
                print(f"Guardo l'utente: {users[0]}")
                furhat.attend(user=users[0])
            else:
                print("Nessun utente rilevato, non guardo nessuno")


            await asyncio.sleep(2)
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



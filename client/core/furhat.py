from furhat_remote_api import FurhatRemoteAPI
import asyncio
import cv2
from .speech_to_text import *


def LaunchFurhatRobot():
    furhat = FurhatRemoteAPI("localhost")
    furhat.set_voice(name='Adriano-Neural')
    furhat.say(text="Ciao! Mi sono attivato correttamente")
    return furhat



async def look(furhat):
    
    try:
        while True:
            
            users = furhat.get_users()


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



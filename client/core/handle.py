import asyncio
import random


EXTROVERT_GESTURES = [
    "BigSmile",
    "Nod",
    "Wink",
    "Frown",
    "Shrug",
    "RollEyes"
]


INTROVERT_GESTURES = [
    "Nod",
    "SmallSmile",
    "Blink",
    "Shrug",
    "HeadShake"
]



async def handle_extrovert(furhat):
    while True:
        gesture = random.choice(EXTROVERT_GESTURES)
        furhat.gesture(name=gesture)

        await asyncio.sleep(random.uniform(3,15))


async def handle_introvert(furhat):
    while True:
        gesture = random.choice(INTROVERT_GESTURES)
        furhat.gesture(name=gesture)

        await asyncio.sleep(random.uniform(3,15))

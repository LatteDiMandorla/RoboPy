import asyncio
import random


def dispatch_traits(traits):
    function_to_execute = []
    for trait in traits:
        function = traits_function_map.get(trait)
        if function: 
            function_to_execute.append(function)
    return function_to_execute

async def execute_functions(furhat, function_to_execute):
    while True:
        random.shuffle(function_to_execute)
        for func in function_to_execute:
            print(f" Eseguo: {func.__name__}")
            await func(furhat)
            await asyncio.sleep(2)  





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

stability = {
    "class": "furhat.gesture.Gesture",
    "frames": [
        {
            "time": [0.0],
            "params": {
                "NECK_TILT": 0.0,
                "SMILE": 0.2,
                "EYEBROW_UP": 0.1
            }
        },
        {
            "time": [1.5],
            "params": {
                "NECK_TILT": 0.05,
                "SMILE": 0.3,
                "EYEBROW_UP": 0.0
            }
        }
    ]
}

def handle_extrovert(furhat):
    furhat.gesture(body=extrovert)

def handle_introvert(furhat):
    furhat.gesture(body=introvert)

def handle_friendly(furhat):
    furhat.gesture(body=friendly)

def handle_unfriendly(furhat):
    furhat.gesture(body=unfriendly)

def handle_conscious(furhat):
    furhat.gesture(body=conscious)

def handle_impulsive(furhat):
    furhat.gesture(body=impulsive)

def handle_stability(furhat):
    furhat.gesture(body=stability)

def handle_instability(furhat):
    random_number = random.randint(1,7)

    match random_number:
        case 1:
            handle_friendly(furhat)
        case 2:
            handle_unfriendly(furhat)
        case 3:
            handle_extrovert(furhat)
        case 4:
            handle_introvert(furhat)
        case 5:
            handle_conscious(furhat)
        case 6:
            handle_impulsive(furhat)
        case 7:
            handle_stability(furhat)




traits_function_map = {
    "Estroverso": handle_extrovert,
    "Introverso": handle_introvert,
    "Amichevole": handle_friendly,
    "Scontroso": handle_unfriendly,
    "Coscienzioso": handle_conscious,
    "Impulsivo": handle_impulsive,
    "Stabile": handle_stability,
    "Instabile": handle_instability,
}




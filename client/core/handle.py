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


async def handle_friendly(furhat):
    print("Prova")


async def handle_unfriendly(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_conscious(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_impulsive(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_stability(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_instability(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_open(furhat):
    furhat.gesture(name="BrowRaise")

async def handle_close(furhat):
    furhat.gesture(name="BrowRaise")





traits_function_map = {
    "Estroverso": handle_extrovert,
    "Introverso": handle_introvert,
    "Amichevole": handle_friendly,
    "Scontroso": handle_unfriendly,
    "Coscienzioso": handle_conscious,
    "Impulsivo": handle_impulsive,
    "Stabile": handle_stability,
    "Instabile": handle_instability,
    "Aperto di mente": handle_open,
    "Chiuso di mente": handle_close
}

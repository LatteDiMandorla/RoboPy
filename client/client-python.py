import socket
import random
import asyncio
from furhat_remote_api import FurhatRemoteAPI
from core.CalcoloTipi import ConvertDictionaryToJson
from core.InputUtenteTipi import chiedi_risposte, mostra_risultati
from core.conversation import run_conversation
from core.furhat import LaunchFurhatRobot
from core.furhat import look
import json


# JUST FOR TESTING

def handle_extrovert(furhat):
    print("Viene effettivamente eseguito")
    furhat.gesture(name="BrowRaise")

def handle_introvert(furhat):
    furhat.gesture(name="BrowRaise")

def handle_friendly(furhat):
    furhat.gesture(name="BrowRaise")

def handle_unfriendly(furhat):
    furhat.gesture(name="BrowRaise")

def handle_conscious(furhat):
    furhat.gesture(name="BrowRaise")

def handle_impulsive(furhat):
    furhat.gesture(name="BrowRaise")

def handle_stability(furhat):
    furhat.gesture(name="BrowRaise")

def handle_instability(furhat):
    furhat.gesture(name="BrowRaise")

def handle_open(furhat):
    furhat.gesture(name="BrowRaise")

def handle_close(furhat):
    furhat.gesture(name="BrowRaise")

BUFFER_SIZE = 4096
SERVER_IP = "127.0.0.1"
PORT = 8081

def send_and_receive_from_server(json_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connessione al server...")
            s.connect((SERVER_IP, PORT))
            
            print("Invio JSON al server...")
            s.sendall(json_data.encode('utf-8'))
            
            print("Attendo risposta dal server...")
            response = s.recv(BUFFER_SIZE)
            json_str = response.decode('utf-8')
            data = json.loads(json_str)
            
            prompt_base = data["prompt base"]
            traits = data["personalità"]
            
            print("Risposta dal server ricevuta correttamente")
            return prompt_base, traits
            
    except socket.error as e:
        print(f"Errore di connessione: {e}")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return None, None
    except Exception as e:
        print(f"Errore generico: {e}")
        return None, None

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
            print(f"👉 Eseguo: {func.__name__}")
            func(furhat)
            await asyncio.sleep(2)  

async def main():
    furhat = LaunchFurhatRobot()
    
    task1 = asyncio.create_task(look(furhat))
    
    risposte = chiedi_risposte()
    
    mostra_risultati(risposte)
    
    json_data = ConvertDictionaryToJson(risposte)
    
    prompt_base, traits = send_and_receive_from_server(json_data)
    
    if prompt_base is None or traits is None:
        print("The error comes from the server communication")
        return
    
    print("Dati ricevuti dal server:", prompt_base, traits)
    
    function = dispatch_traits(traits)
    task2 = asyncio.create_task(execute_functions(furhat, function))
    
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)

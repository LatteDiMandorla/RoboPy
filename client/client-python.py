import socket
import random
import asyncio
from furhat_remote_api import FurhatRemoteAPI
from core.CalcoloTipi import ConvertDictionaryToJson
from core.InputUtenteTipi import mostra_risultati
from core.conversation import run_conversation
from core.furhat import LaunchFurhatRobot
from core.furhat import look
from core.furhat import chiedi_risposte
import json
from core.handle import *



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


async def main():

    furhat, risposte = LaunchFurhatRobot()
    
    task1 = asyncio.create_task(look(furhat))
    
    risposte = chiedi_risposte(furhat)
    
    mostra_risultati(risposte)
    
    json_data = ConvertDictionaryToJson(risposte)
    
    prompt_base, traits = send_and_receive_from_server(json_data)
    
    if prompt_base is None or traits is None:
        print(" Errore nella comunicazione con il server")
        return
    
    print("Dati ricevuti dal server:", prompt_base, traits)
    
    function = dispatch_traits(traits)
    task2 = asyncio.create_task(execute_functions(furhat, function))
    run_conversation(furhat, prompt_base, traits)
    
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)

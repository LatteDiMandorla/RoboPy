import socket
import random
import asyncio
from core.handle import *
from furhat_remote_api import FurhatRemoteAPI
from core.CalcoloTipi import ConvertDictionaryToJson
from core.InputUtenteTipi import mostra_risultati
from core.conversation import run_conversation
from core.furhat import LaunchFurhatRobot
from core.furhat import look
from core.furhat import chiedi_risposte
import json
from core.utils import send_and_receive_from_server
from core.handle import *
import sounddevice as sd



async def main():


    furhat, risposte = LaunchFurhatRobot()
    
    task = look(furhat)
    
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
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)

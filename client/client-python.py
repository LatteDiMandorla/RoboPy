import socket
from core.CalcoloTipi import ConvertDictionaryToJson
from core.InputUtenteTipi import chiedi_risposte, mostra_risultati
from core.run_conversation import Run_conversation


BUFFER_SIZE = 4096
SERVER_IP = "127.0.0.1"
PORT = 8080

def receive_from_server(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))


        response = s.recv(BUFFER_SIZE)
        json_str = response.decode('utf-8')
        data = json.loads(json_str)

        prompt_base = data["prompt base"]
        traits = data["personalità"]

        return prompt_base, traits


traits_function_map = {
    "Estroverso": handle_extrovert,
    "Introverso": handle_introvert,
    "Amichevole": handle_friendly,
    "Scontroso": handle_unfriendly,
    "Coscienzioso": hanlde_conscious,
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
        random.shaffle(function_to_execute)
        for func in function_to_execute:
            await func(furhat)

def ClientCreationSocket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 8080)
    client_socket.connect(server_address)

    return client_socket

def SendJsonToServer(json_data):
    client_socket = ClientCreationSocket()

    try:
        client_socket.sendall(json_data.encode('utf-8'))

        response = client_socket.recv(1024)
        print("Risposta dal server:", response.decode('utf-8'))

    finally:
        client_socket.close()
    

async def main():
    risposte = chiedi_risposte()
    mostra_risultati(risposte)
    json_data = ConvertDictionaryToJson(risposte)
    SendJsonToServer(json_data)
    prompt_base, traits = receive_from_server()
    function = dispatch_traits(traits)
    
    task1 = asyncio.create_task(execute_functions(furhat, function))
    task2 = asyncio.create_task(run_conversation(furhat, prompt_base, traits))

    await asyncio.gather(task1, task2)


    
    
if __name__ == "__main__":
   asyncio.run(main())

import socket
from core.CalcoloTipi import ConvertDictionaryToJson
from core.InputUtenteTipi import chiedi_risposte, mostra_risultati


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



def execute_functions(function_to_execute):
    # Implement logic to execute functions in a pseudo-random order,
    # maybe with threads.


def ClientCreationSocket():
    # Crea il socket del client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connetti al server (indirizzo IP del server e porta)
    server_address = ('127.0.0.1', 8080)  # localhost e porta 8080
    client_socket.connect(server_address)

    return client_socket

def SendJsonToServer(json_data):
    client_socket = ClientCreationSocket()

    try:
        # Invia un messaggio al server
        client_socket.sendall(json_data.encode('utf-8'))

        # Ricevi la risposta dal server
        response = client_socket.recv(1024)
        print("Risposta dal server:", response.decode('utf-8'))

    finally:
        # Chiudi la connessione
        client_socket.close()
    

def main():
    risposte = chiedi_risposte()
    mostra_risultati(risposte)
    json_data = ConvertDictionaryToJson(risposte)
    SendJsonToServer(json_data)
    prompt_base, traits = receive_from_server()
    
if __name__ == "__main__":
    main()

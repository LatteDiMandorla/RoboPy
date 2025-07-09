import socket
import json
import os

SERVER_IP = os.getenv("SERVER_HOST", "server")
PORT = int(os.getenv("SERVER_PORT", 8081))
BUFFER_SIZE = 4096            

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

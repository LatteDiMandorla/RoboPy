<<<<<<< HEAD
import socket
import json

SERVER_IP = "127.0.0.1"       
PORT = 12345                  
BUFFER_SIZE = 4096            

def receive_from_server(): 
    with socket.socket(socket.AF_INET, socket.STREAM) as s:
        s.connect((SERVER_IP, PORT))


        response = s.recv(BUFFER_SIZE)
        json_str = response.decode('utf-8')
        data = json.loads(json_str)

        prompt_base = data["prompt base"]
        traits = data["personalita"]

        return prompt_base, traits
=======
>>>>>>> 5887dbc (feat: add return type to decide_personality.)

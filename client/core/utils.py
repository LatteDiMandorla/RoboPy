import socket


def recive_from_server(): 
    with socket.socket(socket.AF_INET, socket.STREAM) as s:
        s.connect((SERVER_IP, PORT))


        response = s.recv(BUFFER_SIZE)
        json_str = response.decode('utf-8')
        data = json.loads(json_str)

        prompt_base = data["prompt base"]
        traits = data["personalità"]

        return prompt_base, traits

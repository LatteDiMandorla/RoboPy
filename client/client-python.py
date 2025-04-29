import socket

# Crea il socket del client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connetti al server (indirizzo IP del server e porta)
server_address = ('127.0.0.1', 8080)  # localhost e porta 8080
client_socket.connect(server_address)

try:
    # Invia un messaggio al server
    message = "Ciao, server! Sono il client Python."
    client_socket.sendall(message.encode('utf-8'))

    # Ricevi la risposta dal server
    response = client_socket.recv(1024)
    print("Risposta dal server:", response.decode('utf-8'))

finally:
    # Chiudi la connessione
    client_socket.close()


def SendJsonToServer(json_data):
    client_socket = ClientCreationSocket()

    try:
        # Invia un messaggio al server
        messaggio = f"Questo è il risultato del test Tipi: {json_data}"
        client_socket.sendall(messaggio.encode('utf-8'))

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
    
if __name__ == "__main__":
    main()
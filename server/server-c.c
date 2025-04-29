#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main() {
    // Crea il socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configura l'indirizzo del server
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(8080); // Porta
    server_address.sin_addr.s_addr = INADDR_ANY;
    memset(server_address.sin_zero, 0, sizeof(server_address.sin_zero)); // Pulizia del padding

    // Associa il socket all'indirizzo
    int bind_status = bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address));
    if (bind_status == -1) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Mette il server in ascolto
    int listen_status = listen(server_socket, 5);
    if (listen_status == -1) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Server in ascolto sulla porta 8080...\n");

    // Accetta una connessione dal client
    struct sockaddr_in client_address;
    socklen_t client_address_len = sizeof(client_address);
    int client_socket = accept(server_socket, (struct sockaddr *)&client_address, &client_address_len);
    if (client_socket == -1) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }

    // Comunica con il client
    char buffer[1024];
    int recv_status = recv(client_socket, buffer, sizeof(buffer), 0);
    if (recv_status == -1) {
        perror("Receive failed");
        exit(EXIT_FAILURE);
    }
    printf("Client: %s\n", buffer);

    // Risposta al client
    char *message = "Ciao, client! Ho ricevuto il tuo messaggio.";
    int send_status = send(client_socket, message, strlen(message), 0);
    if (send_status == -1) {
        perror("Send failed");
        exit(EXIT_FAILURE);
    }

    // Chiude la connessione
    close(client_socket);
    close(server_socket);

    return 0;
}

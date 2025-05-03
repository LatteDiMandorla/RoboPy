#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 12345
#define BUFFER_SIZE 1024


int main() {

    /* Creation of an endpoint of comunication,
     * AF_INET is for IPv4, SOCK_STREAM is 
     * for the socket type, 0 is a standard protocol number for
     * TCP.                                                       */
    
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }


    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;
    memset(server_address.sin_zero, 0, sizeof(server_address.sin_zero)); 

    int bind_status = bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address));
    if (bind_status == -1) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    int listen_status = listen(server_socket, 5);
    if (listen_status == -1) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Server in ascolto sulla porta 8080...\n");
    

    /* Accepting clients comunication */

    while (1)
    {
       struct sockaddr_in client_address;
       socklen_t client_address_len = sizeof(client_address);
       
       int client_scoket = accept(server_socket, (struct sockaddr *)& client_address, &client_address_len);
       if (client_socket == -1)
       {
          perror("Accept failed!");
          continue;

       }
       
       /* INET_ADDRSTRLEN is a costant variable, defined into <arpa/inet.h>, it's equal
        * to 16, and it's the maximum amount necessary to store an IPv4 adress as a string. */ 

       char client_ip[INET_ADDRSTRLEN];

       /* Converts a binary IP, stored in struct sockaddr_in, to a string. */ 

       inet_ntop(AF_INET, &(client_address.sin_addr), client_ip, INET_ADDRSTRLEN);
       
       char buffer[BUFFER_SIZE];

       int recv_status = recv(client_scoket, buffer, sizeof(buffer) - 1, 0);
       if (recv_status > 0)
       {
          buffer[recv_status] = '\0';
          

       }

       close(client_socket);

    }
       close(server_socket);

    return 0;
}

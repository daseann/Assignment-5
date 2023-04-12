import socket

def main():
    server_ip = input("Enter server IP address: ")
    server_port = int(input("Enter server port number: "))
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    
    print("Server is waiting for connections...")
    
    while True:
        connection, client_address = server_socket.accept()
        print("Connection established with client:", client_address)
        
        while True:
            message = connection.recv(1024).decode()
            
            if not message:
                break
            
            print("Client message:", message)
            response = message.upper()
            connection.send(response.encode())
        
        connection.close()
        print("Connection closed with client:", client_address)

if __name__ == "__main__":
    main()

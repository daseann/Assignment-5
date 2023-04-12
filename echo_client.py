import socket

def main():
    server_ip = input("Enter server IP address: ")
    server_port = int(input("Enter server port number: "))
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((server_ip, server_port))
    except Exception as e:
        print("Error connecting to server:", e)
        return
    
    print("Connected to server.")
    
    while True:
        message = input("Enter message to send (type 'quit' to exit): ")
        
        if message.lower() == 'quit':
            break
            
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print("Server reply:", response)
    
    client_socket.close()

if __name__ == "__main__":
    main()

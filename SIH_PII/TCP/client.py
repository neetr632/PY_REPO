import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
client_socket.connect(server_address)

try:
    while True:
        print("Enter your message:")
        message = input()
        client_socket.sendall(message.encode('utf-8'))
        
        response = client_socket.recv(1024)
        print(f"Received response from server: {response.decode('utf-8')}")
        
    
finally:
    client_socket.close()
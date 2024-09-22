import socket 
# create a tcp/ip socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the address and host to the socket
server_address = ('', 65432)
server_socket.bind(server_address) 

# Listen for incoming connections
server_socket.listen(1)

print(f"the server is running on {server_address}")

while True:
  # wait for a connection
  connection , client_address = server_socket.accept()
  try:
      print(f"connection from {client_address}")
      while True: 
        data = connection.recv(1024)
        if data:
          print(f"Received Message: {data.decode('utf-8')}")
          response = "Message Received"
          connection.send(response.encode('utf-8'))
        else:
          break
  finally:
       connection.close()
    
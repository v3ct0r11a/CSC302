import socket

#client setup
HOST = "127.0.0.1"      #server address
PORT = 65432            #server port

#create socket (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))     #Connect to server

#send request
message = "Hello Server!"
client_socket.sendall(message.encode())

#receive response
response = client_socket.recv(1024).decode()
print(f"Server Response: {response}")

#close connection
client_socket.close()
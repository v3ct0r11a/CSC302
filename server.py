import socket
#server setup
HOST = "127.0.0.1"   #Local host
PORT = 65432   #Port to listen on 

#create socket (IPv4 + TCP)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))    #bind to address
server_socket.listen()    #start listening

print(f"server listening on {HOST}:{PORT}")
while True:
    conn, addr = server_socket.accept()   #Accept connection
    print(f"Connected by {addr}")

    #receive message from client 
    data = conn.recv(1024).decode()
    print(f"Received: {data}")

    #send response
    response = "Hello from Server!"
    conn.sendall(response.encode())

    #close connection
    conn.close()
    
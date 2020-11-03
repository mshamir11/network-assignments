import socket

IP_ADDRESS ="127.0.0.1"
PORT = 12346
BUFFER = 1024

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS,PORT))
print("hello")

while True:
    message =input("Enter a message to the server")
    client_socket.send(bytes(message,'utf-8'))
    data = client_socket.recv(BUFFER)
    print(data.decode('utf-8'))
    if message=="exit":
        break
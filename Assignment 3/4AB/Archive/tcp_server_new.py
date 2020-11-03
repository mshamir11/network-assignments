import socket
import threading


IP_ADDRESS ="127.0.0.1"
PORT = 12344
BUFFER = 1024
NEW_PORT = PORT

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP_ADDRESS,PORT))
server_socket.listen(5)

def CheckAddr(port):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = False
    try:
        server_socket.bind((IP_ADDRESS,port))
        result = True
    except :
        result=False
    server_socket.close()
    return result


def Alloc(port):
    global NEW_PORT
    
    while True:
        NEW_PORT +=1
        if (CheckAddr(NEW_PORT)):
            return NEW_PORT
    


def thread_send(client_socket,address):
    while True:
        data = client_socket.recv(BUFFER)
        print(data)
        message =input("Enter a message to the server")
        client_socket.send(bytes(message,'utf-8'))
         
        if message=="exit":
            break

while True:
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Available_PORT = Alloc(NEW_PORT)
    server_socket.bind((IP_ADDRESS,Available_PORT))
    server_socket.listen(5)
    client_socket,address = server_socket.accept()
    t = threading.Thread(target=thread_send,args=[client_socket,address])
    t.start()
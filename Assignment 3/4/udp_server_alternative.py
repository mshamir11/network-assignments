import socket
import os
import json
import threading
from _thread import start_new_thread

#Variables
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT_NO = 12345
BUFFER = 1024
RESULT_PATH ='./results/udp_ip_address_and_port.json'
PROTOCOL = 'UDP'
NEW_PORT = PORT_NO

# Creating a dictionary of names to get files from index numbers coming from the client
file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name


# f= open(RESULT_PATH, 'w')
# f.close() 
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

def send_data(available_server_port,address):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP_ADDRESS,available_server_port))
    while True:
        print("Im waiting")
        data,address = server_socket.recvfrom(32)
        
        if (address):
            break
    
    f= open(RESULT_PATH, 'a') 
    print(f"Connection with {address} has been establish")
    index = int(data.decode('utf-16'))
    book_name = index_to_names[index]
    book_path = './text_files/'+book_name
    book_size = os.path.getsize(book_path)
    server_socket.sendto(bytes(book_name[:-4]+str(book_size),'utf-16'),address)
    print(f"Client Requested to sent {book_name[:-4]}")
    with open(book_path) as file:
        print("Started to read the file")
        message = str(1)
        
        while (len(message)>0):
            message = file.read(BUFFER)
            server_socket.sendto(bytes(message,'utf-16'),address)
    
    dictionary = {"Client IP_address":address[0],"Client Port":address[1],"Server IP":IP_ADDRESS,"Server port":available_server_port,"Protocol":PROTOCOL,"Book_Name":book_name[:-4]}
    f.write(',\n' + json.dumps(dictionary))
    f.close()
    print("I'm done with the sending. Enjoy you book!")
        
    
    
while True:
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP_ADDRESS,PORT_NO))
    print("I'm Listening...")
    data,address = server_socket.recvfrom(32)
    if (data.decode('utf-8')=='start'):
        available_server_port = Alloc(NEW_PORT)
        server_socket.sendto(bytes(str(available_server_port),'utf-8'),address)
        server_socket.close()
    
    start_new_thread(send_data,(available_server_port,address))
    print(f"New connection established with {address} on Server Port {available_server_port}")
    
    
    
    
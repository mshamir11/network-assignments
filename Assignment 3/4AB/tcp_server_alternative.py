import socket
import os
import argparse
import json
import time
from _thread import *
import threading
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-b","--buffer",help="buffer capacity")
args = vars(ap.parse_args())


#Variables
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT_NO = 12345
PROTOCOL = 'TCP'
BUFFER = 32
NEW_PORT = PORT_NO
RESULT_PATH ='./results/tcp_ip_address_and_port.json'

if RESULT_PATH[10:] not in os.listdir("./results"):
    file = open(RESULT_PATH,'w')
    print(RESULT_PATH[10:])
    file.close()


else:
    file = open(RESULT_PATH,'r+')
    string = file.read()
    file.close()
    if (string[:-1]==']'):
        
        file = open(RESULT_PATH,'w')
        file.write(string[:-1])
        file.close()

#server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)


# Creating a dictionary of names to get files from index numbers coming from the client
file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name

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
    print("im here")
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP_ADDRESS,available_server_port))
    server_socket.listen(5)
    while True:
        print("Im waiting")
        client_socket,address = server_socket.accept()
        
        if (address):
            break
    index = (client_socket.recv(10)).decode('utf-8')
    print(f"Cleint Requested to sent {index_to_names[int(index)]}")
    book_name = index_to_names[int(index)]
    book_path = './text_files/'+book_name
    book_size = os.path.getsize(book_path)
    client_socket.send(bytes(book_name[:-4]+str(book_size),'utf-8'))
    
    
    with open(book_path,'rb') as file:
        message = file.read(BUFFER)
        print("Started to read the file")
        while (len(message)>0):
            client_socket.send(message)
            time.sleep(0.0001)
            message = file.read(BUFFER)
            
            
            # client_socket.setsockopt(socket.SOL_TCP,socket.TCP_QUICKACK,True)
    
    dictionary = {"Client IP_address":address[0],"Client Port":address[1],"Server IP":IP_ADDRESS,"Server port":available_server_port,"Protocol":PROTOCOL,"Book_Name":book_name[:-4]}
        
    file = open(RESULT_PATH,'r+')
    string = file.read()
    file.close()
    if (string[:-1]==']'):
        
        file = open(RESULT_PATH,'w')
        file.write(string[:-1])
        file.close()
    
    with open(RESULT_PATH, 'r+') as f:
        for i in range(1):
            
            if len(f.read()) == 0:
                f.write('['+json.dumps(dictionary))
            else:
                f.write(',\n' + json.dumps(dictionary))
        f.write(']')
        f.close()
    
    
   
    print("Hey Client, I'm done with the sending. Enjoy your book!")
    
 
while True:
    
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP_ADDRESS,PORT_NO))
    server_socket.listen(5)
    print("Im listenting")
    client_socket,address = server_socket.accept()
    #Allocation of Port at the server side
    data = client_socket.recv(32)
    if (data.decode('utf-8')=='start'):
        available_server_port = Alloc(NEW_PORT)
        client_socket.send(bytes(str(available_server_port),'utf-8'))
        client_socket.close()
    
    
    start_new_thread(send_data,(available_server_port,address))
    # t = threading.Thread(target=send_data,args=[client_socket,address])
    # t.start()
    print(f"New connection established with {address} on Server Port {available_server_port}")
    
    # time.sleep(0.0001) ##100 microseconds
     
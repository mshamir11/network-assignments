'''
Reference:
https://github.com/gulshan-mittal/Socket-Programming/blob/master

'''
import socket
import time
import os
import argparse


#Argument Parser Section
ap =argparse.ArgumentParser()
ap.add_argument("-i","--index",help ="index to the dictionary")
ap.add_argument("-p","--persistent",help ="1 for persistent 0 for non persistent")
args = vars(ap.parse_args())

#variables

HOST = socket.gethostname()
PORT = 12345
BUFFER = 1024

file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name



server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(5)

    
def fileSend(client_socket,file_indices):
    
    print("im here")
    
    try:
        filename = index_to_names[int(file_indices.decode())]
        sendFile = open('./text_files/'+filename,'rb')
        client_socket.send(bytes("---File Present---"+filename,'utf-8'))
        
        
    except IOError:
        client_socket.send(bytes("---File Not Present---",'utf-8'))
        return

    ack= client_socket.recv(64)
    print(f"Started to send {filename}")
    read_data=sendFile.read(BUFFER)
    while (read_data):
        
            client_socket.send(read_data)
            ack = client_socket.recv(64)
            read_data=sendFile.read(BUFFER)
    
    sendFile.close()
 
    client_socket.send(bytes("EOF",'utf-8'))
   
    
    
def nonPersistentConnection():
    client_socket, address = server_socket.accept()
    server_socket.settimeout(None)
    print(f"connection to {address} has been established")
    file_indices= client_socket.recv(1024)
    
    fileSend(client_socket,file_indices)
    
    
    print("Finished Sending")
    client_socket.close()
    print(f"connection with {address} is closed")
    

def persistentConnection():
    
    client_socket, address = server_socket.accept()
    client_socket.settimeout(10)
    print(f"connection to {address} has been established")
    
    file_indices = client_socket.recv(32)
    
    while file_indices:
        
        print(f"Client Requested to send {file_indices}")
        fileSend(client_socket,file_indices)
        
        file_indices = client_socket.recv(1024)
        print(file_indices)
    print("Finished Sending all files")
    client_socket.close()
    print("Connection Closed")

print("Server listening....")
while True:
    
    start_time = time.time()
    #nonPersistentConnection()
    
    if args['persistent']=='1':
        print("persistent Connection")
        persistentConnection()
    
    elif args['persistent']=='0':
        print("Non Persistent Connection")
        nonPersistentConnection()
        
    final_time = time.time()
    
    print(f"Total time on the server side {final_time - start_time}")

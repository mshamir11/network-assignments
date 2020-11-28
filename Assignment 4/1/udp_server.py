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

IP_ADDRESS = "127.0.0.1"
PORT = 12345
ADDRESS = (IP_ADDRESS,PORT)
BUFFER = 1024

file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name



server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(ADDRESS)


    
def fileSend(file_indices,address):
    
    print("im here")
    
    try:
        filename = index_to_names[int(file_indices.decode())]
        sendFile = open('./text_files/'+filename,'rb')
        
        server_socket.sendto(bytes("---File Present---"+filename,'utf-8'),address)
        print("hi")
        
        
    except IOError:
        server_socket.sendto(bytes("---File Not Present---",'utf-8'),address)
        return
    
    print(f"Started to send {filename}")
    server_socket.sendto(bytes("---File Present---"+filename,'utf-8'),address)
    
    ack,_ =server_socket.recvfrom(100)
    ack,_ =server_socket.recvfrom(100)
    ack,_ =server_socket.recvfrom(100)
    read_data=sendFile.read(BUFFER)
    
    while (read_data):
        
           server_socket.sendto(read_data,address)
           ack = server_socket.recvfrom(64)
           read_data=sendFile.read(BUFFER)
    
    sendFile.close()
 
    server_socket.sendto(bytes("EOF",'utf-8'),address)
   
    
    
def nonPersistentConnection():
    
    
    data,address = server_socket.recvfrom(4)
    server_socket.settimeout(None)
    print(f"connection to {address} has been established")
    
    
    fileSend(data,ADDRESS)
    
    
    print("Finished Sending")
    print(f"connection with {address} is closed")
    server_socket.close()

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
    
    if args['persistent']=='1':
        print("persistent Connection")
        persistentConnection()
        print("hi")
        break
    elif args['persistent']=='0':
        print("Non Persistent Connection")
        nonPersistentConnection()
        break
        
    final_time = time.time()
    
    print(f"Total time on the server side {final_time - start_time}")

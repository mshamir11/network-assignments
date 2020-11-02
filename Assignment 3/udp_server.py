import socket
import os

buff = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),12345))

#creating a dictionary mapping to get book names from ids
file_list = os.listdir('./text_files')
id_to_names ={}
for i,item in enumerate(file_list):
    id_to_names[i]=item


while True:
    data,adress = sock.recvfrom(4096)
    print(data.decode("utf-8"))
    
    with open('./text_files/'+id_to_names[int(data)]) as file:
        message = file.read(buff)
    message = "Welcome to UDP server"
    print(data)
    sock.sendto(bytes(message,'utf-8'),adress)
    
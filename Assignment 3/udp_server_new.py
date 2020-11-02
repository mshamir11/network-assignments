import socket
import os

IP_ADDRESS = socket.gethostname()
PORT = 12345
bind_address = (IP_ADDRESS,PORT)
BUFFER = 1024


file_list = os.listdir('./text_files')
id_to_names ={}

for i,item in enumerate(file_list):
    id_to_names[i]=item

server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_sock.bind((IP_ADDRESS,PORT))
#server_sock.bind((IP_ADDRESS,PORT))

while True:
   
    # data,address = server_sock.recvfrom(4096)
    # print("data received:",data.decode('utf-16'))
    
   
    # message = "Hey this is server".encode('utf-16')
    # server_sock.sendto(bytes(message),address)
    
    # with open("./text_files/war_and_peace.txt") as file:
    #     message =str(1)
    data,address = server_sock.recvfrom(4096)
    print(data.decode("utf-16"))
    
    with open('./text_files/'+id_to_names[int(data.decode("utf-16"))]) as file:
        message = str(1)
        # print("total pages",len(file.read()))
        while (len(message)>0):
            message =file.read(BUFFER)
            server_sock.sendto(bytes(message,'utf-16'),address)
    
    print("hello, im done")     
        
server_sock.close()


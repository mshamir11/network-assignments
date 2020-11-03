import socket
import os
import json
import threading

#Variables
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT_NO = 12345
BUFFER = 1024
RESULT_PATH ='./results/udp_ip_address_and_port.json'
PROTOCOL = 'UDP'
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((IP_ADDRESS,PORT_NO))

# Creating a dictionary of names to get files from index numbers coming from the client
file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name


# f= open(RESULT_PATH, 'w')
# f.close() 


def send_data(data,address):
    
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
    
    dictionary = {"Client IP_address":address[0],"Client Port":address[1],"Server IP":IP_ADDRESS,"Server port":PORT_NO,"Protocol":PROTOCOL,"Book_Name":book_name[:-4]}
    f.write(',\n' + json.dumps(dictionary))
    f.close()
    print("I'm done with the sending. Enjoy you book!")
        
    
    
while True:
    print("I'm Listening...")
    data,address = server_socket.recvfrom(32)
    t= threading.Thread(target=send_data,args=[data,address])
    t.start()
    
    
    
    
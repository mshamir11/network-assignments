import socket
import os
import argparse
import json
import time
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-b","--buffer",help="buffer capacity")
args = vars(ap.parse_args())


#Variables
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT_NO = 12345
PROTOCOL = 'TCP'
BUFFER = 1024
RESULT_PATH ='./results/tcp_ip_address_and_port.json'

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS,PORT_NO))
server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
server_socket.listen(5)

# Creating a dictionary of names to get files from index numbers coming from the client
file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name

def send_data(socket,address):
    index = (client_socket.recv(10)).decode('utf-16')
    
    print(f"Cleint Requested to sent {index_to_names[int(index)]}")
    book_name = index_to_names[int(index)]
    book_path = './text_files/'+book_name
    book_size = os.path.getsize(book_path)
    client_socket.send(bytes(book_name[:-4]+str(book_size),'utf-16'))
    f= open(RESULT_PATH, 'a') 
    
    with open(book_path) as file:
        message = str(1)
        print("Started to read the file")
        while (len(message)>0):
            message = file.read(BUFFER)
            client_socket.send(bytes(message,'utf-16'))
            # client_socket.setsockopt(socket.SOL_TCP,socket.TCP_QUICKACK,True)
    
    dictionary = {"Client IP_address":address[0],"Client Port":address[1],"Server IP":IP_ADDRESS,"Server port":PORT_NO,"Protocol":PROTOCOL,"Book_Name":book_name[:-4]}
        
    
    client_socket.send(bytes("\00",'ascii'))
    
    f.write(",\n"+json.dumps(dictionary))
    f.close()
    print("Hey Client, I'm done with the sending. Enjoy your book!")
    
 
while True:
    print("Im listenting")
    client_socket,address = server_socket.accept()
    t = threading.Thread(target=send_data,args=[client_socket,address])
    t.start()
    print(f"Connection with {address} has been establish")
    
    # time.sleep(0.0001) ##100 microseconds
     
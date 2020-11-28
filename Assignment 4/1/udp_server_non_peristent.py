import socket
import os



#Variables
IP_ADDRESS = socket.gethostname()
PORT = 12345
BUFFER = 1024

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((IP_ADDRESS,PORT))

# Creating a dictionary of names to get files from index numbers coming from the client
file_name_list = os.listdir('./text_files')
index_to_names = {}
for key,name in enumerate(file_name_list):
    index_to_names[key]=name

while True:
    print("I'm Listening...")
    
    data,address = server_socket.recvfrom(32)
    print(f"Connection with {address} has been establish")
    index = int(data.decode('utf-16'))
    book_name = index_to_names[index]
    book_path = './text_files/'+book_name
    server_socket.sendto(bytes(book_name[:-4],'utf-16'),address)
    print(f"Client Requested to sent {book_name[:-4]}")
    with open(book_path,'rb') as file:
        print("Started to read the file")
        message = "rst"       
        while (len(message)>0):
            message = file.read(BUFFER)
            server_socket.sendto(message,address)
    print("I'm done with the sending. Enjoy you book!")
import socket
import os
import argparse
import time
import json
import re
import subprocess

#Argument Parser Section
ap =argparse.ArgumentParser()
ap.add_argument("-i","--index",help ="index to the dictionary")
ap.add_argument("-b","--buffer",help="buffer capacity")
ap.add_argument("-r","--result",help="output result path")
args = vars(ap.parse_args())

#Variables
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT_NO = 12345
PROTOCOL = 'TCP'
INDEX = args['index'] 
BUFFER = int(args['buffer'])
RESULT_PATH = args['result']

start_time = time.time()
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)

client_socket.connect((IP_ADDRESS,PORT_NO))

client_socket.send(bytes("start",'utf-8'))
port = int(client_socket.recv(32).decode('utf-8'))
print (port)
client_socket.close()
time.sleep(1)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
client_socket.connect((IP_ADDRESS,port))
# Sending the index of the required file to the server
client_socket.send(bytes(INDEX,'utf-8'))
print(f"Index {INDEX} searching in the server")
book_and_size = (client_socket.recv(100)).decode('utf-8')
book_and_size_list =re.split('(\d+)',book_and_size)
book = book_and_size_list[0]
book_size = book_and_size_list[1] 
print(f"Found {book} with index {INDEX}")

# Opening the output file and creating the file name
pid = str(os.getpid())
output_path ='./received_files/'+book+'_'+PROTOCOL+'_'+pid+'.txt'
write_file = open(output_path,'wb')
print(f"Started receiving the file")

signal =True


while signal:
    
    

# client_socket.setsockopt(socket.SOL_TCP,socket.TCP_QUICKACK,True)
    try:
        temp_message = client_socket.recv(BUFFER)
        
        
       
        
        
        if (len(temp_message)<=0):
            break
        # message += temp_message
        write_file.write(temp_message)
        # print(f"Time elapsed: {time.time() - start_time}s")
        client_socket.settimeout(0.001)
    except:
        break
   
            
    
write_file.close()
final_time = time.time() - start_time
print(f"it took {final_time}s to receive the file")
print(f" {book} received completely using TCP protocol with {BUFFER} bytes buffer. Thanks server!")
size_of_file = os.path.getsize(output_path)
through_put = size_of_file/final_time
word_count = subprocess.check_output(f"cat {output_path} | wc -w",shell=True)
word_count = (word_count.decode())[:-1]
dictionary = {"Book_Name":book,"Protocol":PROTOCOL,"PID":pid,"Buffer_Size":BUFFER,"Total_Time_Taken":final_time,"Throughput":through_put,"Word_Count":word_count}

with open(RESULT_PATH, 'a') as f:
    
    f.write(",\n"+json.dumps(dictionary))
    f.close()
        
        
    
    


    
        
 
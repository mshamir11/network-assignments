import socket
import os
import argparse
import time
import json
import re
import subprocess

#argument parser to get input from command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", help = "index to the dictionary")
ap.add_argument("-b", "--buffer", help = "index to the dictionary")
ap.add_argument("-r", "--result", help = "path to the output")
args = vars(ap.parse_args())


#Variables
IP_ADDRESS = socket.gethostname()
PORT = 12345
BUFFER = int(args['buffer'])
INDEX = args['index']
PID = str(os.getpid())
PROTOCOL = 'UDP'
RESULT_PATH =args['result']

start_time = time.time()
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(f"Requesting server to send the file with index {int(INDEX)}")
client_socket.sendto((bytes(INDEX,'utf-16')),(IP_ADDRESS,PORT))
data,address = client_socket.recvfrom(200)

book_and_size = data.decode('utf-16')
book_and_size_list =re.split('(\d+)',book_and_size)
book = book_and_size_list[0]
book_size = book_and_size_list[1] 
print(f"Started receiving {book}")

full_message = bytes('','utf-16')

while True:
    
    try:
        data,address = client_socket.recvfrom(BUFFER)
        full_message += data
        print(f"Time Elapsed: {time.time() - start_time}")
        print(len(data))
        client_socket.settimeout(1)
        
    except  socket.timeout:
        break
print(f"Successfully Recieved {book} using UDP protocol with {BUFFER} size")
output_path = './received_files/'+book+'_'+PROTOCOL+'_'+PID+'.txt'
write_file =open(output_path,"w") 
write_file.write(full_message.decode('utf-16'))
final_time = time.time() - start_time

size_of_file = os.path.getsize(output_path)
through_put = size_of_file/final_time
word_count = subprocess.check_output(f"cat {output_path} | wc -w",shell=True)
word_count = (word_count.decode())[:-1]
dictionary = {"Book_Name":book,"Protocol":PROTOCOL,"PID":PID,"Buffer_Size":BUFFER,"Total_Time_Taken":final_time,"Original Size":book_size,"Size_of_the_file_created":size_of_file,"Throughput":through_put,"Word_Count":word_count}

with open(RESULT_PATH, 'r+') as f:
    if len(f.read()) == 0:
        f.write('['+json.dumps(dictionary))
    else:
        f.write(',\n' + json.dumps(dictionary))

client_socket.close()

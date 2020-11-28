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
BUFFER = 1024

PID = str(os.getpid())
PROTOCOL = 'UDP'
RESULT_PATH = './results/udp_results.json'

start_time = time.time()
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for INDEX in range(5):
    
    client_socket.sendto((bytes(str(INDEX),'utf-16')),(IP_ADDRESS,PORT))
    data,address = client_socket.recvfrom(200)
    book = data.decode('utf-16')
    
    print(f"Started receiving {book}")

    output_path = './received_files/'+book+'_'+PROTOCOL+'_'+PID+'.txt'
    write_file =open(output_path,"wb") 

    while True:
        
        try:
            data,address = client_socket.recvfrom(BUFFER)
            write_file.write(data)
            print(f"Time Elapsed: {time.time() - start_time}")
            client_socket.settimeout(0.1)
            
        except  socket.timeout:
            print(f"Successfully Recieved {book} using UDP protocol with {BUFFER} size")
            
            
            final_time = time.time() - start_time
            
            size_of_file = os.path.getsize(output_path)
            through_put = size_of_file/final_time
            word_count = subprocess.check_output(f"cat {output_path} | wc -w",shell=True)
            word_count = (word_count.decode())[:-1]
            dictionary = {"Book_Name":book,"Protocol":PROTOCOL,"PID":PID,"Buffer_Size":BUFFER,"Total_Time_Taken":final_time,"Size_of_the_file_created":size_of_file,"Throughput":through_put,"Word_Count":word_count}
            
            with open(RESULT_PATH, 'r+') as f:
                if len(f.read()) == 0:
                    f.write('['+json.dumps(dictionary))
                else:
                    f.write(',\n' + json.dumps(dictionary))
            
            
            break
client_socket.close()
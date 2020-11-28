'''
Reference:
https://github.com/gulshan-mittal/Socket-Programming/blob/master

'''

import socket
import time
import os
import json
import subprocess
import sys
import argparse


#Argument Parser Section
ap =argparse.ArgumentParser()
ap.add_argument("-i","--index",help ="index to the dictionary")
ap.add_argument("-p","--persistent",help ="1 for persistent 0 for non persistent")
args = vars(ap.parse_args())



#variable
IP_ADDRESS = "10.0.0.11"
PORT = 12345
BUFFER = 1024
PROTOCOL = "TCP"
RESULT_PATH ='./results/tcp_results.json'
AGG_RESULT_PATH = './results/tcp_agg_results.json'
start_time_single =0
final_time_single =0
connection_setup_start =0
connection_setup_end =0
file_string = args['index']
filenames= file_string.strip().split()
total_size =0
start_time = time.time()


def sendData(client_socket,data):
    try:
        client_socket.send(bytes(data,'utf-8'))
    except socket.error:
        print("Error Sending data")
        sys.exit(1)
    
def fileReceive(client_socket,file_index):
    global start_time_single
    global final_time_single
    global total_size
   
    
    confirm = client_socket.recv(2048).decode()
    filename = confirm[18:]   
    
    if "---File Present---" in confirm[:19]:
        
        print("---File Present---")
        pid = str(os.getpid())
        output_path ='./received_files/'+'_'+PROTOCOL+'_'+pid+'_'+filename
        with open(output_path,'wb') as f:
            print(" File Opened")
            client_socket.send(bytes("OK",'utf-8'))
            print("Receiving Data")
            while True:
                    
                data = client_socket.recv(BUFFER)
                if data==bytes("EOF",'utf-8'):
                    break
               
                f.write(data)    
                sendData(client_socket,'OK')
        
        total_time_single = (time.time()-start_time_single)*1000
        size_of_file = os.path.getsize(output_path)
        total_size += size_of_file
        through_put = size_of_file*1000/total_time_single
        word_count = subprocess.check_output(f"cat {output_path} | wc -w",shell=True)
        word_count = (word_count.decode())[:-1]
        dictionary = {"Book_Name":filename[:-4],"Protocol":PROTOCOL,"PID":pid,"Buffer_Size":BUFFER,"Total_Time_Taken (ms)":total_time_single,"Size_of_the_file_created":size_of_file,"Throughput":through_put,"Word_Count":word_count}
            
        with open(RESULT_PATH, 'r+') as fp:
            if len(fp.read()) == 0:
                fp.write('['+json.dumps(dictionary))
            else:
                fp.write(',\n' + json.dumps(dictionary))
        f.close()
        print(f"Successfully received the file {file_index}")
    else:
        print("File not present")
        

def nonPersistentConnection(IP_ADDRESS,PORT,filenames):
    
    global start_time_single
    
    for file_index in filenames:
        
        start_time_single = time.time()
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((IP_ADDRESS,PORT))
        print(f"Requesting File with index: {file_index}")
        client_socket.send(bytes(file_index,'utf-8'))
        
        fileReceive(client_socket,file_index)
        client_socket.close()
        

def persistentConnection(IP_ADDRESS,PORT,filenames):
    
    global start_time_single
    global connection_setup_start
    global connection_setup_end
    
    
    
    connection_setup_start = time.time()
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP_ADDRESS,PORT))
    connection_setup_end = time.time()
    for file_index in filenames:
        start_time_single = time.time()
        client_socket.send(bytes(file_index,'utf-8'))
        fileReceive(client_socket,file_index)
    
    client_socket.close()
    print('Connection Closed')   
    print(f"Total time taken for setup: {connection_setup_end -connection_setup_start}")
    final_time = time.time()
    
    total_time = final_time -connection_setup_start
    aggregate_throughPut = total_size/total_time
    print(f"Aggregate Download time= {total_time}")
    print(f"Aggregate throughput(Mb/s) = {aggregate_throughPut/1000000}")
    pid = os.getpid()
    agg_dictionary = {"PID":pid,"Total_Time":total_time,"Aggregate_throughput":aggregate_throughPut}
            
    with open(AGG_RESULT_PATH, 'r+') as fp:
        if len(fp.read()) == 0:
            fp.write('['+json.dumps(agg_dictionary))
        else:
            fp.write(',\n' + json.dumps(agg_dictionary))
    fp.close()

if args['persistent']=='1':
    print("persistent Connection")
    persistentConnection(IP_ADDRESS,PORT,filenames)
    
elif args['persistent']=='0':
    print("Non Persistent Connection")
    nonPersistentConnection(IP_ADDRESS,PORT,filenames)  
#

    


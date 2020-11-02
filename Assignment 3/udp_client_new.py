import socket
import os
import argparse

#argument parser to get input from command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", help = "index to the dictionary")
ap.add_argument("-b", "--buffer", help = "index to the dictionary")
args = vars(ap.parse_args())

IP_ADDRESS = socket.gethostname()
PORT = 12345
BUFFER = 1024

#creating a dictionary mapping to get book names from ids
file_list = os.listdir('./text_files')
id_to_names ={}
for i,item in enumerate(file_list):
    id_to_names[i]=item

# Naming the output file
pid = str(os.getpid())
protocol= "udp"
book = (id_to_names[int(args['index'])])[:-4]
write_file =open('./received_files_client/'+book+'_'+protocol+'_'+pid+'.txt',"w") 


bind_address = (IP_ADDRESS,PORT)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

#client_socket.bind(bind_address)


# data,adress = client_socket.recvfrom(1024)
# print(data)
index  = args['index']

send_data = str(index)
client_socket.sendto(send_data.encode('utf-16'),bind_address)
message = bytes("",'utf-16')
count =0
while True:
    
   
    
    try:
     
        data,address = client_socket.recvfrom(BUFFER)
        message += data
        count +=1024
       # print(data)
        print(count)
        client_socket.settimeout(0.1)
           
    except socket.timeout:
       
        
        write_file.write(message.decode('utf-16'))
        client_socket.close()  
        
        break     
 
        
    
 
        
    
    

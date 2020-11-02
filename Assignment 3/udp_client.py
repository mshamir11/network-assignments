import socket
import os
import argparse



#argument parser to get input from command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", help = "index to the dictionary")
ap.add_argument("-b", "--buffer", help = "index to the dictionary")
args = vars(ap.parse_args())


#creating a dictionary mapping to get book names from ids
file_list = os.listdir('./text_files')
id_to_names ={}
for i,item in enumerate(file_list):
    id_to_names[i]=item

# Naming the output file
pid = str(os.getpid())
protocol= "tcp"
book = (id_to_names[int(args['index'])])[:-4]
write_file =open('./received_files_client/'+book+'_'+protocol+'_'+pid+'.txt',"w") 

buff = 1024

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP_IP = socket.gethostname()
UDP_PORT= 12345
index  = args['index']

#client_sock.sendto(index.encode("utf-8"),(socket.gethostname(),12345))

data , address = client_sock.recvfrom(4096)
print(str(data))
message = "hey this is client"
client_sock.sendto(bytes(message,'utf-8'),address)
import socket
import os
import argparse


#argument parser to get input from command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", help = "index to the dictionary")
ap.add_argument("-b", "--buffer", help = "index to the dictionary")
args = vars(ap.parse_args())


#connection to the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),12345))
HEADERSIZE = 10



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

first = str(args['index'])
s.send(bytes(first,'utf-16'))
full_msg =bytes('','utf-16')
count =0
while True:
    
    try:
        msg = s.recv(int(args['buffer']))
        full_msg +=msg
        s.settimeout(0.01)
        count += 1024
        print (count)
    except socket.timeout:
        write_file.write(full_msg.decode('utf-16'))
        s.close()
        break
        
        





# while True:
#     full_msg = bytes('','utf-16')
#     new_msg = True
#     full_message =0
#     count =0
#     first = str(args['index'])
#     s.send(bytes(first,'utf-16'))
#     while (full_message==0):
#         msg = s.recv(int(args['buffer']))
        
#         if new_msg:
            
#             msg_len = int(msg[:HEADERSIZE])
#             new_msg = False
#         full_msg +=msg
        
#         #print(count)
#         count +=1
#         if (len(full_msg)-HEADERSIZE ==msg_len):
#             print("full message received")
#             print(full_msg[HEADERSIZE:].decode('utf-16'))
#             write_file.write(full_msg)
#             write_file.close()
#             new_msg = True
#             full_msg =''
#             full_message =1
            
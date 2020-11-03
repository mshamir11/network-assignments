import threading
import time
import os


RESULT_PATH ='./results/udp_results.json'
def call_udp(index,buffer,RESULT_PATH):
    command = 'python udp_client.py -i '+str(index)+' -b ' + str(buffer)+' -r '+RESULT_PATH
    os.system(command)

t1 = threading.Thread(target=call_udp,args=[1,32,RESULT_PATH])
t2 = threading.Thread(target=call_udp,args=[2,32,RESULT_PATH])
t2.start()
t1.start()
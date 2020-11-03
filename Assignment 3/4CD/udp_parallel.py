import threading
import time
import os


RESULT_PATH ='./results/udp_simultaneous.json'
def call_udp1(index,buffer,RESULT_PATH):
    command = 'python udp_client1.py -i '+str(index)+' -b ' + str(buffer)+' -r '+RESULT_PATH
    os.system(command)
   
def call_udp2(index,buffer,RESULT_PATH):
    command = 'python udp_client2.py -i '+str(index)+' -b ' + str(buffer)+' -r '+RESULT_PATH
    os.system(command)
t1 = threading.Thread(target=call_udp1,args=[3,32,RESULT_PATH])   
t2 = threading.Thread(target=call_udp2,args=[5,32,RESULT_PATH])
t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()


import threading
import time
import os
from _thread import *



RESULT_PATH ='./results/tcp_results.json'
def call_tcp1(index,buffer,RESULT_PATH):
    command = 'python tcp_client1.py -i '+str(index)+' -b ' + str(buffer)+' -r '+RESULT_PATH
    os.system(command)
   
def call_tcp2(index,buffer,RESULT_PATH):
    command = 'python tcp_client2.py -i '+str(index)+' -b ' + str(buffer)+' -r '+RESULT_PATH
    os.system(command)
t1 = threading.Thread(target=call_tcp1,args=[3,32,RESULT_PATH])   
t2 = threading.Thread(target=call_tcp2,args=[5,32,RESULT_PATH])
t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()




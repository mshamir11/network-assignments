import threading
import time
import os
from _thread import *


def call_thread1():
    command = 'python tcp_client_new.py -i "1" -p 0'
    os.system(command)
    
def call_thread2():
    command = 'python tcp_client_new.py -i "2" -p 0'
    os.system(command)
def call_thread3():
    command = 'python tcp_client_new.py -i "3" -p 0'
    os.system(command)
def call_thread4():
    command = 'python tcp_client_new.py -i "4" -p 0'
    os.system(command)
def call_thread5():
    command = 'python tcp_client_new.py -i "5" -p 0'
    os.system(command)
   
t1 = threading.Thread(target=call_thread1)   
t2 = threading.Thread(target=call_thread2)
t3 = threading.Thread(target=call_thread3)
t4 = threading.Thread(target=call_thread4)
t5 = threading.Thread(target=call_thread5)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


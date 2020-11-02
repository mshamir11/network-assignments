import os
import pandas as pd

'''
Experiment 2
Without Delayed Ack and Without Nagle: Only on Client

Run tcp_server.py
'''


RESULT_PATH ='./results/tcp_results_without_delayedAck_withoutNagle_OnlyOnClient.json'
buffer_list = ['32']
file = open(RESULT_PATH,'w')
for item in buffer_list:
    for i in range(1):
        command = 'python tcp_client_without_DelayAck_withoutNagle.py -i '+str(3)+' -b ' + item+' -r ' + RESULT_PATH
        print(command)
        os.system(command)

with open(RESULT_PATH,'a') as f:
    f.write(']')

df =pd.read_json(RESULT_PATH)
print(df)
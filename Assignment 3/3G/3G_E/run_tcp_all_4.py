import os
import pandas as pd

# buffer_list = ['32768','65536']
RESULT_PATH ='./results/tcp_results_without_delayedAck_OnBoth.json'
buffer_list = ['65536']
file = open(RESULT_PATH,'w')
for item in buffer_list:
    for i in range(1):
        command = 'python tcp_client_without_DelayAck.py -i '+str(3)+' -b ' + item+' -r ' + RESULT_PATH
        print(command)
        os.system(command)

with open(RESULT_PATH,'a') as f:
    f.write(']')

df =pd.read_json(RESULT_PATH)
print(df)
import os
import pandas as pd



# buffer_list = ['32768','65536']
RESULT_PATH ='./results/udp_results.json'
buffer_list = ['1024']
file = open(RESULT_PATH,'w')

for i in range(6):
    command = 'python udp_client.py -i '+str(i)+' -b ' + buffer_list[0]+' -r ' + RESULT_PATH
    print(command)
    os.system(command)

with open(RESULT_PATH,'a') as f:
    f.write(']')

df =pd.read_json(RESULT_PATH)
print(df)
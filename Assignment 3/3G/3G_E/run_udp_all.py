import os
import pandas as pd

RESULT_PATH ='./results/udp_results_with_word_count_1024.json'
buffer_list = ['32','1024','32768','65536']
file =open (RESULT_PATH,'w')
for item in buffer_list:
    for i in range(6):
        command = 'python udp_client.py -i '+str(i)+' -b ' + item+' -r '+RESULT_PATH
        os.system(command)




with open(RESULT_PATH,'a') as f:
    f.write(']')

df =pd.read_json(RESULT_PATH)
print(df)
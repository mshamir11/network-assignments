# Instructions for running the experiment

## 3ABC
### How to run the file.

TCP:
1. run tcp_server.py
    ```
       python tcp_server.py
    ```

2. run tcp_client.py with necessary arguments
   Here 0 is the index of the file and 1024 is buffer size
    ```
      python tcp_client.py -i 0 -b 1024
    ```
UDP:

3. run udp_server.py
    ```
       python udp_server.py
    ```

4. run udp_client.py with necessary arguments
   Here 0 is the index of the file and 1024 is buffer size
    ```
      python tcp_client.py -i 0 -b 1024
###### Please Note that the code is written for this directory. Please try to ensure the directory names are not changed.

## 3 EFG

For the first two experiments.
TCP:
1. run tcp_server.py.
    ```
       python tcp_server.py
       
    ```

2. run tcp_clients. I have written a script to call the terminal commants in some of the files to conduct the experiment smoothely and to reproduce it effectively.
    ```
       python run_tcp_all_1.py
       python run_tcp_all_2.py
       
    ```
For the next two experiments. Change the server used. 
    run tcp_server_without_<problem specificname>.py.
    ```
       python tcp_server_without_<provlem specific name>.py
       
    ```
     ```
       python run_tcp_all_3.py
       python run_tcp_all_4.py
       
    ```

All the four experiments can be done in the similar way. For UDP, replace all the tcp in the above with udp. and run the experiment


## 4 ABCD

For TCP:

1. run the tcp_server_alternate.py
2. run the clients to connect to. Any number of clients can be connected to the server at the same time. Just need to call the function from different terminals.
Here -i indicates the index of the book. -b the buffer size. -r where to store the output result
    ```
      python tcp_client1.py -i 0 -b 1024 -r ./results/tcp_result.json
      python tcp_client1.py -i 1 -b 1024 -r ./results/tcp_result.json
    ```
3. run simultaneously. After running the tcp server. Run the below code.
    ```
      python tcp_parallel.py
    ```

For UDP:
replace tcp by udp in the tcp section. and run the code.

======================================================================================================

### Note:
1. All the results can be seen in the results folder as json files.
2. Keep the names of the directories as it is.
3. Compile_result.ipynb jupyter notebook can be used to analyze the result in dataframe.
4. This assignment is a part of Assignments of course CS 433 - Computer Networks
## TCP Server Client Steps
=====================================================================
### How to run the file.

1. run tcp_server.py
    ```
       python tcp_server.py
    ```

2. run tcp_client.py with necessary arguments
   Here 0 is the index of the file and 1024 is buffer size
    ```
      python tcp_client.py -i 0 -b 1024
    ```
###### Please Note that the code is written for this directory. Please try to ensure the directory names are not changed.
======================================================================
### Server Side:
tcp_server.py

1. import necessary packages
    ```sh 
    import socket
    ```
2. Connect to the ipv4 type adress as well as tcp protocol.
    Here, SOCK_STREAM is for TCP protocol, for UDP you need to use SOCK_DGRAM
    ```sh
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ```
3. Connect to the IP address and listen for the clients
    In our case, IP_ADRESS = "127.0.0.1" or socket.gethostname()
                 PORT No.  = 12345
    ```
    server_socket.bind("IP_ADDRESS",PORT NO)
    server_socket.listen(5)
    ```
4. Accept Connection Request from the client
    ```
    client_socket, address = server_socket.accept()
    ```
5. To receive Message:
   buffer = size of the file in bytes you wish to receive at a time.
   The message received would be a bytes objects. To decode use message.decode('utf-16')
    ```
    message = client_socket.recv(buffer)
    ```
6. To send a Message:
   Here message is a string and utf-16 is the encoding.
    ```
      client_socket.send(bytes(message,'utf-16'))
    ```
=========================================================================
### Client Side:
tcp_client.py

1. import packages
    ```
    import socket
    import os
    import argparse
    import time
    ```
2. Use Argparse to take inputs from the terminal and convert it to a dictionary
    ```
    ap =argparse.ArgumentParser()
    ap.add_argument("-i","--index",help ="index to the dictionary")
    ap.add_argument("-b","--buffer",help="buffer capacity")
    args = vars(ap.parse_args())
    ```
3. Define IP and TCP protocol
    ```
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ```
4. Connect to a server IP address and Port
```
   client_socket.connect((IP_ADDRESS,PORT_NO))
```
5. To receive Message:
   buffer = size of the file in bytes you wish to receive at a time.
   The message received would be a bytes objects. To decode use message.decode('utf-16')
    ```
    message = client_socket.recv(buffer)
    ```
6. To send a Message:
   Here message is a string and utf-16 is the encoding.
    ```
      client_socket.send(bytes(message,'utf-16'))
    ```
7. Record Time
```
   start_time = time.time()
   end_time = time.time()- start_time
```
==================================================================================
==================================================================================
==================================================================================
# UDP Programme
### How to run the file.

1. run udp_server.py
    ```
       python udp_server.py
    ```

2. run udp_client.py with necessary arguments
   Here 0 is the index of the file and 1024 is buffer size
    ```
      python udp_client.py -i 0 -b 1024
    ```
###### Please Note that the code is written for this directory. Please try to ensure the directory names are not changed.
udp_server.py

1. import packages and connect to the respective IP_ADDRESS and PORT.
SOCK_DGRAM -> UDP protocol
    ```
    import socket
    import os
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP_ADDRESS,PORT)
    ```
2. To receive data
Here buffer is the amount of data that needs to be recieve at single time.
    ```
    server_socket.recvfrom(buffer)
    ```
3. To send data
here address is the ip address of the client with the port information
    ```
    server_socket.sendto(bytes(messages,'utf-16'),address)
    ```



==========================================================================
udp_client.py

1. import packages and connet to IPv4 and UDP protocol
    ```
    import socket
    import os
    import argparse
    import time
    
    client.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ```
2. Argument Parser
    ```
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--index", help = "index to the dictionary")
    ap.add_argument("-b", "--buffer", help = "index to the dictionary")
    args = vars(ap.parse_args())
    ```
3. To send a message
Here address, is the address of the server
address =(IP_ADDRESS,PORT)
    ```
    client_socket.sendto(bytes(messages,'utf-16'),address)
    ```
 4. To receive a message
    ```
    data,address = client_socket.recvfrom(buffer)
    ```
5. To find time
    ```
        start_time = time.time()
        end_time = time.time() - stat_time()
    ```
    



===============================================================
#### Run Commands from python scripts

    ```
    import os
    os.system("python tcp_client.py -i 0 -b 1024 -r ./results/tcp_results.json")
    ```
#### To get values from the terminal commands

Here, "f"cat {output_path} | wc -w",shell=True" is the command. It gives the word count of the file at the address output_path

    ```
        import subprocess
        subprocess.check_output(f"cat {output_path} | wc -w",shell=True)
    ```

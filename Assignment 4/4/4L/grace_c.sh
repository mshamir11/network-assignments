server1 python3.8 tcp_server_sc_thread1.py -p 0 &
server2 python3.8 tcp_server_sc_thread2.py -p 0 &
server3 python3.8 tcp_server_sc_thread3.py -p 0 &
H python3.8 tcp_client1.py -p 0 -i "1" &
I python3.8 tcp_client1.py -p 0 -i "2" &
J python3.8 tcp_client2.py -p 0 -i "3" &
K python3.8 tcp_client3.py -p 0 -i "4" 




















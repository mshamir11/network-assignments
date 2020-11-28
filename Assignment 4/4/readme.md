## Instructions to run the code


### Python files with "topology" in its name would be a python mininet CLI implementation

#### To run that code. Open Mininet. 
```
   $ sudo python <the_topology_file>.py

```

#### Once mininet is executed. To check various nodes and IP addresses. Use

```
  >mininet dump
```


#### To run the server and client in the respective nodes



```
  >mininet server tcp_server.py -p 0 
```
Here the server, is the host name in the network topology
```
   >mininet client1 tcp_client.py -p 0 -i "5"
```

Here client1 is the host name of client in the mininet network topology. -p 0 for non persistent connection and -i "5" for downloading file with index 5

#### To use <filename>.sh to run multiple commands at the same time
```
   >mininet source <filename>.sh
```

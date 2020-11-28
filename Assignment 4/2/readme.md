## Instructions to run the code


### To start the server

-p 1 --> for persistent
-p 0 --> for non persistent

```
python tcp_server_new.py -p 1
```
#### To start thread based concurrent server:

-p 1 --> for persistent
-p 0 --> for non persistent
```
python tcp_server_sc_thread.py -p 1
```

#### To start fork based concurrent server:
-p 1 --> for persistent
-p 0 --> for non persistent
```
python tcp_server_sc_fork.py -p 1
```

### To start the client

here -i "indexes of files separated by space" --> for downloading 5 books.
-p 1 --> persistent
-p 0 --> Non Persistent

```
python tcp_client_new.py -p 1 -i "1 2 3 4 5"
```



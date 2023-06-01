# py-socket-thing

## usage
You'll need atleast two terminals for this.

One of these will be the server, the others will be the clients.

The terminals may be both running on your computer, or on seperate computers in the same network (sharing a WiFi, or connected in a LAN).

### terminal 1
This will act as our server
```
python src/server.py
```
Once the server starts it'll await a client connection.

### terminal 2
This will be one of the clients.
```
python src/client.py <server address>
```

Server address is the address of the device (computer or mobile) on which the server is running. This can be checked from the settings app.

## note
the server can connect with only one client at a time.

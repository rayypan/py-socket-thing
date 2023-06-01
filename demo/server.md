This is the server side of messages.
For the client's side, see [client.md](client.md).

```
~/py-socket-thing $ py server.py

server: 0.0.0.0:8080: waiting for client
server: 127.0.0.1:49580: client connected
[127.0.0.1:49580]: hi there
[you]: hi
[127.0.0.1:49580]: how do you do?
[you]: totally fine, how about you?
[127.0.0.1:49580]: fine as always
[you]: ok then, see ya
server: 127.0.0.1:49580: client closed connection
server: 0.0.0.0:8080: waiting for client
server: 127.0.0.1:49582: client connected
[127.0.0.1:49582]: hi im your next client
[you]: hello there how can i help you?
[127.0.0.1:49582]: nevermind
[you]: ok
server: 127.0.0.1:49582: client closed connection
server: 0.0.0.0:8080: waiting for client
```

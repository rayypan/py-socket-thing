The following is the client side of messages.
For the server's side, see [server.md](server.md)

```
~/py-socket-thing $ py client.py 0.0.0.0

[you]: hi there
[0.0.0.0:8080]: hi
[you]: how do you do?
[0.0.0.0:8080]: totally fine, how about you?
[you]: fine as always
[0.0.0.0:8080]: ok then, see ya
[you]: end

~/py-socket-thing $ py client.py 0.0.0.0

[you]: hi im your next client
[0.0.0.0:8080]: hello there how can i help you?
[you]: nevermind
[0.0.0.0:8080]: ok
[you]: end

~/py-socket-thing $ 
```

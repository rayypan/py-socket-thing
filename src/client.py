#!/bin/env python3

import socket        # socket functions
import sys           # system functions
import signal        # signal handling

try:
    import readline  # richer input
except ImportError:
    pass

SOCK_BACKLOG = 1     # accept one connection at a time
RECV_SIZE    = 4096  # max length of recieved data

def client(ipv4net, port = 8080):
    cli_sock = socket.socket()
    cli_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cli_sock.connect((ipv4net, port))
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    message = input('[you]: ').strip()
    while len(message) < 1:
        message = input('[you]: ').strip()
    while message.lower().strip() != 'end':
        cli_sock.send(message.encode())
        print('awaiting reply...', end='')
        sys.stdout.flush()
        data = str(cli_sock.recv(RECV_SIZE).decode())
        print('\r[{}:{}]: {}'.format(ipv4net, port, data))
        message = input('[you]: ').strip()
        while len(message) < 1:
            message = input('[you]: ').strip()
    cli_sock.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('client: missing args: provide a server ip')
        sys.exit(1)
    elif len(sys.argv) > 2:
        client(sys.argv[1], int(sys.argv[2]))
    else:
        client(sys.argv[1])

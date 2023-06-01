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

def server(port = 8080):
    host = '0.0.0.0'
    srv_sock = socket.socket()
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((host, port))

    def sig_handler(sig, frame):
        srv_sock.close()
        sys.exit(0)
    signal.signal(signal.SIGINT, sig_handler)

    while True:
        print('server: {}:{}: waiting for client'.format(host, port))
        srv_sock.listen(SOCK_BACKLOG)
        (conn, address) = srv_sock.accept()  # accept new connection
        print('server: {}:{}: client connected'.format(address[0], address[1]))
        while True:
            print('awaiting reply...', end='')
            sys.stdout.flush()
            data = str(conn.recv(RECV_SIZE).decode())
            if not data:
                print('\rserver: {}:{}: client closed connection'.format(address[0], address[1]))
                break
            print('\r[{}:{}]: {}'.format(address[0], address[1], data))
            data = input('[you]: ').strip()
            while len(data) < 1:
                data = input('[you]: ').strip()
            conn.send(data.encode())
        conn.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        server()
    else:
        server(int(sys.argv[1]))

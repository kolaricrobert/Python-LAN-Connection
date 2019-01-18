#!/usr/bin/env python3

import socket

HOST = 'HOST_TO_CONNECT'  # Edit this field with the ip address to which the server is started
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
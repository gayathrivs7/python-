#!/usr/bin/env python3

import socket

s=socket.socket()
port=12346
host=socket.gethostbyname("localhost")
s.connect((host,port))
print(s.recv(1025))
s.close()

#!/usr/bin/env python3

import socket

s=socket.socket()
port=12346
s.bind(('',port))
s.listen(5)
while True:
    c,add =s.accept()
    print(addr)
    print(c)
    c.send("thank u for conncting")
    c.close()

    

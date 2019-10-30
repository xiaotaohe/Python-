# coding=utf8

import socket
import datetime

HOST='127.0.0.1'
PORT=3434
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
s.connect((HOST,PORT))
print("Connect %s:%d OK"%(HOST,PORT))
data=""
data = s.recv(1024).decode()
print("Receive: ",data)
s.close()

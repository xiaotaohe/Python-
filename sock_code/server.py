# coding=utf8

import socket
import datetime

HOST='0.0.0.0'
PORT=3434

#创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定
s.bind((HOST,PORT))
s.listen(1)

print("server start..............")
while True:
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    print(dt)
    conn,addr=s.accept()   #接受客户端连接
    print('Client %s connected!'%str(addr)) #输出客户端的IP地址
    message = 'Current time is '+str(dt)
    conn.sendall(message.encode())#向客户端发送当前时间
    print("Sent: ",message)
    conn.close()

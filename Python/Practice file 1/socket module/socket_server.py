#Coding practice by Telusko

import socket

s= socket.socket()
print('Socket created')


s.bind(('localhost',9999)) #range of port numbers (0->65535)

s.listen(3) #3 clients -  3 connections
print('waiting for connections')

while True: #keep it running continuously.
    c, addr = s.accept() #give client socket - address
    print('connected with -', addr ,'\n',c)

    c.send(bytes('Hello world!','utf-8')) #sending data in bytes - utf 8 format

    c.close()
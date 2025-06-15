import socket

#Create a socket
s = socket.socket()

#Get current machine name
host = socket.gethostname()

#Client wants to connect to server's port number 9999
port = 9999

#1024 is the buffer size or max amount of data to be received at once
s.connect((host,port))
#port(s.recv(1024))
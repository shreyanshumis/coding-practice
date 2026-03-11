import socket

c = socket.socket()

c.connect(('localhost',9999))

print(c.recv(1024).decode()) #using receive function - Buffer size || decode does not print the 'b'(bytes format) before the message
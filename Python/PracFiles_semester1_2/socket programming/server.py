import socket

#Create socket object
s= socket.socket()

#Get current machine name
host = socket.gethostname()

#get port no. for connection
port = 9999

s.bind((host,port))

print("Waiting for connection...")
s.listen(5)

#Connect and accept from client
while True:
    conn,addr = s.accept()
    print('Got connection from', addr)
    print(conn)

    #close the connection
    conn.close()
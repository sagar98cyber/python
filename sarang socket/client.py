# Client Connection Code
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Syntax: client.connect((serveraddress, serverport))
c.connect((socket.gethostname(), 1024))

# Code Ends

msg = c.recv(1024)
print(type(msg))
print(msg.decode("utf-8"))
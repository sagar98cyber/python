#Connection and Server Establishment Code

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Syntax: s.bind((ipaddress/host, port))
# To Deploy Server
s.bind((socket.gethostname(), 1024))
#Syntax: s.listen(no of connection)
#To allow Client to connect
s.listen(5)

# Code Ends

#Logic for Client Server Communication
while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket Programming in Python", "utf-8"))
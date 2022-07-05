#Connection and Server Establishment Code

from f_transfer_server import receiveFile
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
    clt.send(bytes("1. To Recieve\n 2. To Send", "utf-8"))
    choice = clt.recv(1024).decode()
    print(f'{choice} : {type(choice)}')
    if choice == '1':
        clt.send(bytes("Recieve", "utf-8"))
        
    elif choice == '2':
        clt.send(bytes("Send", "utf-8"))
    else:
        clt.send(bytes("Wrong", "utf-8"))
    
    



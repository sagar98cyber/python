"""
Server receiver of the file
"""
#import socket
#import tqdm
import os

# device's IP address
#SERVER_HOST = "0.0.0.0"
#SERVER_PORT = 1024

# receive 4096 bytes each time
BUFFER_SIZE = 4096

SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
#s = socket.socket()
# bind the socket to our local address
#s.bind((SERVER_HOST, SERVER_PORT))
# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
#s.listen(5)
#print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accept connection if there is any
#client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
#print(f"[+] {address} is connected.")
'''
def receiveFile():
# receive the file infos
# receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    #progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            #progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    # close the server socket
    #s.close()
 '''       

def recieve_file_client(client_socket):
    print(f'FLAG 2:f_transfer_client')
# receive the file infos
# receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    print(f'FLAG 3: recieved : {received}')
    filename, filesize, realFileName = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    #progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    os.remove(realFileName)
    print(f'FLAG 4:f_transfer_client')
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            print(f'FLAG 5:f_transfer_client')
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            #progress.update(len(bytes_read))
    os.rename(filename,realFileName)
    # close the client socket
    print(f'FLAG 6:f_transfer_client')
    client_socket.close()
    # close the server socket
    #s.close()
        

def send_file_client(client_socket):       
    print(f'FLAG 2:f_transfer_client')
    received = client_socket.recv(BUFFER_SIZE).decode()
    print(f'FLAG 3: recieved : {received}')
    exists = check_if_file_exist(filename=received)
    if exists == True :
        print(f'FLAG 4: File Exists')
        client_socket.send(bytes("Exists","utf-8"))
        print(f'FLAG 5: Sent')
    else:
        print(f'FLAG 4: File does not Exists')
        client_socket.send(bytes("No Exists","utf-8"))


def check_if_file_exist(filename):
    path_name = filename
    if os.path.exists(path_name):
        #print("File exists")
        return True
    else:
        #print("File does not exist")
        return False
"""
Client that sends the file (uploads)
"""
import socket
#import tqdm
import os
#import argparse

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4


def send_file(filename,host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    #progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            #progress.update(len(bytes_read))

    # close the socket
    s.close()

def send_file_server(filename,s,realFileName):
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{realFileName}".encode())
    print(f'Flag 2 f transfer client')
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            print(f'flag 3:  {bytes_read}')
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            print(f'FLAG 4')
            # update the progress bar
            #progress.update(len(bytes_read))

    # close the socket
    s.close()

def checkIfFileExists(filename,c):
    #send the filename to server
    c.send(bytes(str(filename),'utf-8'))
    #check if the file exists in the response
    msg = c.recv(1024)
    print(msg.decode("utf-8"))
    if msg.decode("utf-8") == "Exists":
        print(f'Flag 2: f_transfer_client : calling retrieveFile()')
        retrieveFile(filename=filename,c=c)
    else:
        print(f'File does not exist on the server please check the file name and try again')
        c.close()

def retrieveFile(filename,c):
    pass
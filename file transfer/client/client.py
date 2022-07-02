"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4

#def encrypt_file_rsa_algo_public_key(bytes):

def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    #filename = encrypt_file_rsa_algo_public_key(filename)
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            #before  transmission read all the bytes encrypt it
            #bytes_read = encrypt_file_rsa_algo_public_key(bytes_read)
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the socket
    s.close()

fileName = input("Enter the filename you want to send.\n If it is in the same directory then share the \"relative path\" or if it is not in the current working directory share the \"absolute path\" of the file:\n")
host = input("Enter the HOST ADDRESS you want to connect to:")
port = 5001
send_file(filename=fileName,host=host,port=port)
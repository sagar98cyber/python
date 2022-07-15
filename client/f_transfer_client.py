"""
Client that sends the file (uploads)
"""
import os
#import argparse

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4


'''def send_file(filename,host, port):
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
'''

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
    print(f'FLAG 5 : {filename} : {realFileName}')
    os.remove(filename)
    os.remove(realFileName)

def recieve_file_server(server_socket):
    print(f'FLAG 4:f_transfer_client')
# receive the file infos
# receive using client socket, not server socket
    received = server_socket.recv(BUFFER_SIZE).decode()
    print(f'FLAG 5: recieved : {received} : {type(received)}')
    filename, filesize, realFileName = received.split(SEPARATOR)
    if os.path.exists(filename):
        os.remove(filename)
    if os.path.exists(realFileName):
        os.remove(realFileName)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    #progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    print(f'FLAG 6:f_transfer_client')
    server_socket.send(bytes("Send","utf-8"))
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = server_socket.recv(BUFFER_SIZE)
            print(f'FLAG 7:f_transfer_client')
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            #progress.update(len(bytes_read))
    # close the client socket
    print(f'FLAG 8:f_transfer_client : {realFileName}')
    server_socket.close()
    return filename,realFileName
    # close the server socket
    #s.close()

def checkIfFileExists(filename,c):
    #send the filename to server
    c.send(bytes(str(filename),'utf-8'))
    #check if the file exists in the response
    msg = c.recv(1024)
    print(msg.decode("utf-8"))
    if msg.decode("utf-8") == "Exists":
        print(f'Flag 2: f_transfer_client : calling retrieveFile()')
        #retrieveFile(filename=filename,c=c)
        return True
    else:
        print(f'File does not exist on the server please check the file name and try again')
        c.close()
        return False

def retrieveFile(filename,c):
    print(f'FLAG 3 : Asaking to send the file')
    response = recieve_file_server(c)
    print(f'flag 9 : {response} : {type(response)}')
    return response
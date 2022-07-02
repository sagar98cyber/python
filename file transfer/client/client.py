"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import cipher as c

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 256 * 4
PUBLIC_KEY =""
PRI_KEY=""

def writeOnFilePublic(data):
    file_to_write_on = open("Public.txt", 'w')
    #file_to_write_on.writelines(bytes(data,"utf-8"))
    file_to_write_on.writelines(data)
    return None

def writeOnFilePrivate(data):
    file_to_write_on = open("Private.txt", 'w')
    #file_to_write_on.writelines(bytes(data,"utf-8"))
    file_to_write_on.writelines(data)
    return None

def readPublicFile():
        with open("Public.txt", "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    PUBLIC_KEY = PUBLIC_KEY+ bytes_read
                    if not bytes_read:
                        # file transmitting is done
                        break

def readPrivateFile():
        with open("Private.txt", "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    PRI_KEY = PRI_KEY + bytes_read
                    if not bytes_read:
                        # file transmitting is done
                        break


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
            #print(f"\n\n {type(bytes_read)}")
            if not bytes_read:
                # file transmitting is done
                break
            #before  transmission read all the bytes encrypt it
            #bytes_read = encrypt_file_rsa_algo_public_key(bytes_read)
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the socket
    s.close()

#fileName = input("Enter the filename you want to send.\n If it is in the same directory then share the \"relative path\" or if it is not in the current working directory share the \"absolute path\" of the file:\n")
#host = input("Enter the HOST ADDRESS you want to connect to:")
fileName = "data.csv"
host="127.0.0.1"
port = 5001
secretKey,publicKey = c.keyGen()
print(f"\n\n {secretKey}")
print(f"\n\n {publicKey}")
writeOnFilePublic(str(publicKey))
writeOnFilePrivate(str(secretKey))

send_file(filename=fileName,host=host,port=port)
from f_transfer_client import send_file_server
from encryption_main_client import encryption,decryption
from f_transfer_client import checkIfFileExists, retrieveFile
from get_rsa_keys import get_rsa_keys
from read_bytes_of_file import read_bytes_of_file
from decrypt import decrypt
from write_on_file import write_on_file


def fileToBeSentCheckIfFound(fileNameCheck):
    ###check if the file exists in the directory or not
    var = True
    if var == True:
        return '1'
    else:
        return '0'

def sendFileToServer(fileName,socket):
    print(f'FLAG 1: business logic : {fileName}')
    send_file_server(filename='file_to_write_on.txt',s=socket,realFileName=fileName)

def nameOfFileToBeRetrieved(filename,socket):
    print(f'FLAG 1: business logic : {filename} to be retrived')
    response = checkIfFileExists(filename=filename,c=socket)
    if response == True:
        files = retrieveFile(filename=filename,c=socket)
        decryptFileStart(files[0],files[1])

def decryptFileStart(newFileName,realFileName):
    print(f'FLAG 9 starting decryption : {newFileName} : {realFileName}')
    (private_key, public_key) = get_rsa_keys()
    #encrypted_message = encrypt(normal_message, public_key)
    #write_on_file('file_to_write_on.txt', encrypted_message)
    encrypted_message = read_bytes_of_file(newFileName)
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f'FLAG 10 : {decrypted_message} : {decrypted_message}')
    write_on_file(realFileName, decrypted_message)

    pass
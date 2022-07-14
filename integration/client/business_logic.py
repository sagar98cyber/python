from f_transfer_client import send_file_server
from encryption_main_client import encryption,decryption

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

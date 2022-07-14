# Client Connection Code
import socket
from business_logic import fileToBeSentCheckIfFound,sendFileToServer
from encryption_main_client import decryption, keyGeneration,encryption
#from f_transfer_client import send_file_server
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Syntax: client.connect((serveraddress, serverport))


def exceptionChoice():
    print("\n\nPlease enter a valid choice\n 1. To Recieve\n 2. To Send")
# Code Ends
def fInput(socket):
    intInput = input("Make a Choice")
    if intInput == '1' or intInput == '2':
        c.send(bytes(str(intInput),"utf-8"))
        choice_response = c.recv(1024).decode()
        sInput(choice_response,socket)
    else:
        exceptionChoice()
        fInput(socket)  

def sInput(choice_response,socket):
    #msg = ""
    if choice_response == 'Recieve':
        receiving_file = input('Enter the name of the file to be retrived:')
    elif choice_response == 'Send':
        sendingFileName = input('Enter the name of the file to be sent:')
        result = fileToBeSentCheckIfFound(sendingFileName)
        if result == '1':
            encryption(file_to_read=sendingFileName)
            #send the file to server
            sendFileToServer(fileName=sendingFileName,socket=socket)
        else:
            exceptionChoice()
            fInput() 
    else:
        print('SINPUT888888')
        exceptionChoice()
            
c.connect(('192.168.12.132', 1024))
#while True:    
msg = c.recv(1024)
print(msg.decode("utf-8"))
#keyGeneration()    #GENERATE NEW PUBLIC AND PRIVATE KEYS
fInput(c)
#decryption()
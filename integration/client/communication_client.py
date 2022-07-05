# Client Connection Code
import socket
from business_logic import fileToBeSentCheckIfFound
from encryption_main_client import decryption, keyGeneration,encryption
from f_transfer_client import send_file
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Syntax: client.connect((serveraddress, serverport))
c.connect((socket.gethostname(), 1024))

def exceptionChoice():
    print("\n\nPlease enter a valid choice\n 1. To Recieve\n 2. To Send")
# Code Ends
def fInput():
    intInput = input("Make a Choice")
    if intInput == '1' or intInput == '2':
        c.send(bytes(str(intInput),"utf-8"))
        choice_response = c.recv(1024).decode()
        sInput(choice_response)
    else:
        exceptionChoice()
        fInput()  

def sInput(choice_response):
    #msg = ""
    if choice_response == 'Recieve':
        receiving_file = input('Enter the name of the file to be retrived:')
    elif choice_response == 'Send':
        sendingFileName = input('Enter the name of the file to be sent:')
        result = fileToBeSentCheckIfFound(sendingFileName)
        if result == '1':
            encryption(file_to_read=sendingFileName)
            #send the file to server
            #send_file(sendingFileName,"127.0.0.1",1024)
        else:
            exceptionChoice()
            fInput() 
    else:
        print('SINPUT888888')
        exceptionChoice()
            

#while True:    
msg = c.recv(1024)
print(msg.decode("utf-8"))
#keyGeneration()    #GENERATE NEW PUBLIC AND PRIVATE KEYS
fInput()
decryption()
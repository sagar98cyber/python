# Client Connection Code
import socket

from numpy import true_divide
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
    else:
        print('SINPUT888888')
        exceptionChoice()
            

#while True:    
msg = c.recv(1024)
print(msg.decode("utf-8"))
fInput()
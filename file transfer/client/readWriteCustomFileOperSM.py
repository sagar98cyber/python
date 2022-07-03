import os
from businessLogic import encrypt_file_rsa_algo_public_key,readPublicFile,breakKeys

BUFFER_SIZE = 256

def checkIfTheDirExists1():
    if os.path.isdir("output"): 
        print('exists')
    else: 
        os.mkdir("output")

def fileReadEncryptOutput(fileName):
    #flag
    print(f"Flag 3: FileName:",fileName)
    PublicKey = breakKeys(readPublicFile())
    print(f'PUBLUC KEY IN READ CUSTOM : {type(PublicKey[0])} : {PublicKey} : {type(breakKeys(readPublicFile()))}')
    #with open(fileName, "rb") as in_file, open("out.csv", "wb") as out_file:
    with open(fileName, "rb") as in_file, open(f'output\{fileName}', "wb") as out_file:
       # while True:
            for line in in_file:
                #temp = encrypt_file_rsa_algo_public_key(str(line),PublicKey)
                #out_file.write(temp)
                out_file.write(line)
            #chunk = in_file.read(BUFFER_SIZE)
            #print(f'CHUNK: {type(chunk)}')                         #BYTES OF DATA  
            #temp = encrypt_file_rsa_algo_public_key(str(chunk),PublicKey)
            #if chunk == b"":
            #    break # end of file
                
            #out_file.write(temp)

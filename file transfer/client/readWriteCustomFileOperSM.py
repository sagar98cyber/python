import os

BUFFER_SIZE = 256

def checkIfTheDirExists1():
    if os.path.isdir("output"): 
        print('exists')
    else: 
        os.mkdir("output")

def fileReadEncryptOutput(fileName):
    #flag
    print(f"Flag 3: FileName:",fileName)
    #with open(fileName, "rb") as in_file, open("out.csv", "wb") as out_file:
    with open(fileName, "rb") as in_file, open(f'output\{fileName}', "wb") as out_file:
        while True:
            chunk = in_file.read(BUFFER_SIZE)
            print(type(chunk))    
            if chunk == b"":
                break # end of file
                
            out_file.write(chunk)
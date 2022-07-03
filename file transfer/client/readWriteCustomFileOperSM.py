import os

def checkIfTheDirExists1(fileN):
    fileName = fileN
    if os.path.isdir("output"): 
        print('exists')
    else: 
        os.mkdir("output")

'''#with open(fileName, "rb") as in_file, open("out.csv", "wb") as out_file:
with open(fileName, "rb") as in_file, open(f'output\{fileName}', "wb") as out_file:
    while True:
        chunk = in_file.read(c1.BUFFER_SIZE)
            
        if chunk == b"":
            break # end of file
            
        out_file.write(chunk)
'''


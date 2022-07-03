from businessLogic import readPrivateFile,decrypt_file_rsa_algo_private_key


BUFFER_SIZE = 256
PRI_KEY = readPrivateFile()

with open("output\data.csv", "rb") as in_file:
    while True:
            chunk = in_file.read(BUFFER_SIZE)
            print(f'CHUNK: {type(chunk)}') 
            #print(chunk.decode())                        #BYTES OF DATA  
            temp = decrypt_file_rsa_algo_private_key(chunk.decode(),PRI_KEY)
            if chunk == b"":
                break # end of file
                
            print(temp)


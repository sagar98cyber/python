import cipher as c
import businessLogic as bLogic
from readWriteCustomFileOperSM import checkIfTheDirExists1,fileReadEncryptOutput

BUFFER_SIZE = 256 
PUBLIC_KEY =""
PRI_KEY=""



fileName = "data.csv"
host="127.0.0.1"
port = 5001
secretKey,publicKey = c.keyGen()
#print("F1: ",secretKey,publicKey,type(secretKey))
bLogic.writeOnFilePublic(str(publicKey))
bLogic.writeOnFilePrivate(str(secretKey))

PUBLIC_KEY = bLogic.readPublicFile()
PRI_KEY = bLogic.readPrivateFile()

checkIfTheDirExists1()

fileReadEncryptOutput(fileName)

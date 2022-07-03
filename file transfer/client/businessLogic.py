import cipher as c
def breakKeys(keys1):
    keys1 = keys1.replace('(',"")
    keys1 = keys1.replace(')',"")
    response1 = keys1.split(",")
    print(f" FLAG 3 {keys1} {type(tuple(response1))}")
    a,b = response1
    print(f" FLAG 4 {a} : {b} : {type(int(a))} : {type(int(b))}")
    d = (int(a),int(b))
    print(f" FLAG 5 {d} : {type(d)}")
    return d

def writeOnFilePublic(data): 
    #file_to_write_on = open("file transfer\client\Public.txt", 'w')
    file_to_write_on = open("Public.txt", 'w')
    #file_to_write_on.writelines(bytes(data,"utf-8"))
    file_to_write_on.writelines(data)
    print(f"FLAG 2 Written Files in Public")
    return True

def writeOnFilePrivate(data):
    #file_to_write_on = open("file transfer\client\Private.txt", 'w')
    file_to_write_on = open("Private.txt", 'w')
    #file_to_write_on.writelines(bytes(data,"utf-8"))
    file_to_write_on.writelines(data)
    print(f"FLAG 2 Written Files in Private")
    return True

def readPublicFile():
    TEMP = ""
    #with open("file transfer\client\Public.txt", "r") as f:
    with open("Public.txt", "r") as f:
        for line in f:
            TEMP = TEMP+line
    PUBLIC_KEY = TEMP
    return PUBLIC_KEY
    print(f'FLAG 1: {PUBLIC_KEY} {type(PUBLIC_KEY)}')


def readPrivateFile():
    TEMP = ""
    #with open("file transfer\client\Private.txt", "r") as f:
    with open("Private.txt", "r") as f:
        for line in f:
            TEMP = TEMP+line
    PRI_KEY = TEMP
    return PRI_KEY
    print(f'FLAG 2:  {PRI_KEY} {type(PRI_KEY)}')

def encrypt_file_rsa_algo_public_key(bytes1,PUBLIC_KEY):
    key1 = breakKeys(PUBLIC_KEY)
    print(f"\n\n PUB PUB PUB {PUBLIC_KEY}")
    print(f"\n\n BYTE BYTE BYTE {type(bytes1)} : {bytes1}")
    dataInString = c.encrypt(bytes1,key1)
    print(f'FLAG 7 {type(dataInString)}')
    return bytes(dataInString,"utf-8")
    #return bytes(bytes1,"utf-8")     #returning the same bytes now delete later

import random

def isPrime(x):
    i = 2
    while i*i <= x:          # Only checks for factors up to the square root of x
        if x%i==0:
            return False
        i+=1
    return True

# Generates an n-digit prime number
def primeGenerator(n):
    string = ""
    for i in range(n):
        x=random.randint(1,9)
        string += str(x)
    number = int(string)

    if number%2==0:         # Eliminating even numbers
        number+=1

    while True:
        if isPrime(number):
            return number
        number+=2

# Finds the multiplicative inverse of a mod b
def pulverizer(a,b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = pulverizer(b % a, a)
        d = y - (b // a) * x
        return gcd, d, x

# Generates a secret key and a public key
def keyGen():
    numberOfDigits = 10
    p = primeGenerator(numberOfDigits)        # First random prime number
    q = primeGenerator(numberOfDigits)        # Second random prime number

    n = p*q
    r = (p-1)*(q-1)                           # Euler's Totient
    e = primeGenerator(numberOfDigits)**2     # A number that is highly likely to be relatively prime with r

    publicKey = (e,n)

    g, d, y = pulverizer(e,r)
    if d<0:
        d %= r

    secretKey = (d,n)

    return secretKey, publicKey

def encrypt(message, publicKey):
    print(f"FLAG PRINTING BEFORE : ENCRYPTION : {message} : {type(message)}")
    (e,n) = publicKey
    encryptedMessage = []
    for letter in message:
        letter = ord(letter)
        encryptedLetter = pow(letter, e, n)
        encryptedMessage.append(encryptedLetter)
    #print(f'in encrypt FLAG 6 {type(str(encryptedMessage))} : {encryptedMessage}')
    return str(encryptedMessage)

def decrypt(encryptedMessage, secretKey):
    (d,n) = secretKey
    originalMessage = ""
    originalNumber=0
    print(f'in encrypt FLAG 6 {type(str(encryptedMessage))} : {encryptedMessage}')

    enclistnew=[]
    enclistnew2=[]
    #print("encrypted msg: ",encryptedMessage)

    for i in range(len(encryptedMessage)-1):
        enclistnew2.append(encryptedMessage[i].replace(" ", ""))
        #print("i=",enclistnew2[i])

        enclistnew.append(int(enclistnew2[i]))

    #print(enclistnew)
    for number in enclistnew:
        print("Number and type:",number,type(number))

        #if number != '':
            #if number != ' ': 
                #number = int(number)
                #print(number," ",type(number))
                #print("number::",number)
        originalNumber=pow(number, d, n)
        print("Original Number:",originalNumber)
        #originalMessage+=chr(originalNumber)

        #print(f"{chr(originalNumber)}")
        with open("output_decrpted.csv", "a") as out_file:
            #print(type(originalMessage))
            #out_file.write(originalMessage)
            out_file.write(chr(originalNumber))


        #return originalMessage
            #else:
                #pass
    #print(f"FLAG ORIGNAL MESSAGE : {originalMessage} : {type(originalMessage)}")
    #return originalMessage

#def main():
#    message = bytes(input("Input the message to encrypt: "),"utf-8")
#    print(type(message))
#    message = message.decode()
#    print(type(message))
#    secretKey, publicKey = keyGen()

#    encryptedMessage = encrypt(message,publicKey)

#    print("\nEncrypted text:", encryptedMessage)
#    print("\nThe secret key is:", secretKey)

 #   originalMessage = decrypt(encryptedMessage,secretKey)
 #   print("\nDecrypted Text:", originalMessage)

#main()
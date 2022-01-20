uniqueIPS = []      #all the UNIQUE IPs are gonna be stored in this list
allIps = []         #all the IPS are gonna be stored in this list
allURLS = []        #all the URLS are gonna be stored in this list

def splitFunction(parsedString):                #function to split the string and apppend to the list
    myList = parsedString.split()
    allIps.append(myList[0])
    allURLS.append(myList[10])


with open('apache_logs.txt',buffering=200000) as f:
    for line in f:
        splitFunction(line)

for eachItem in allIps:
    if (eachItem not in uniqueIPS):
        uniqueIPS.append(eachItem)

#print(f'''                         #uncommment this block to see all the IPs, URLs, Unique IPs
#    The IPs ARE: 
#    {allIps}
#    The URLs ARE:
#    {allURLS}
#    The UNIQUE IPs:
#    {uniqueIPS}
#''')

print(f'Length of all IPS: {len(allIps)}')
print(f'Length of all URLS: {len(allURLS)}')
print(f'Length of all unique IPS: {len(uniqueIPS)}')
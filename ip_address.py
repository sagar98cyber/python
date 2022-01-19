allIps = []
allURLS = []
def splitFunction(parsedString):
    myList = parsedString.split()
    allIps.append(myList[0])
    allURLS.append(myList[10])


with open('apache_logs.txt',buffering=200000) as f:
    for line in f:
        splitFunction(line)

#for item in range(0,len(allIps):
#    print(f'{allIps[item]}   {allURLS[item]}')

uniqueIPS = []
for eachItem in allIps:
    if (eachItem not in uniqueIPS):
        uniqueIPS.append(eachItem)


print(f'Length of all IPS: {len(allIps)}')
print(f'Length of all URLS: {len(allURLS)}')
print(f'Length of all unique IPS: {len(uniqueIPS)}')
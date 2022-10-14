from datetime import datetime
from fileinput import filename
dateVal = datetime.today().strftime('%Y-%m-%d')
#print(dateVal)

fileName = f"{dateVal}.log"
print(fileName)

#task 1
with open(f'log files/{fileName}','r',buffering=20000) as f:
    for line in f:
        print(line)


## TASK 2
def readTheMostUpdatedFile(path):
    with open(f'{path}','r',buffering=20000) as f:
        for line in f:
            print(line)

import os

def newest():
    path = os.getcwd() + "\log files"
    #print(f"CWD {path}")
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    print(max(paths, key=os.path.getctime))
    latestFile = max(paths, key=os.path.getctime)
    readTheMostUpdatedFile(latestFile)

newest()
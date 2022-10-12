from datetime import datetime
from fileinput import filename
dateVal = datetime.today().strftime('%Y-%m-%d')
#print(dateVal)

fileName = f"{dateVal}.log"
print(fileName)


with open(f'log files/{fileName}','r',buffering=20000) as f:
    for line in f:
        print(line)
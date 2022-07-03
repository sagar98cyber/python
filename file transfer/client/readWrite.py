import os
fileName = "data.csv"
if os.path.isdir("output"): 
    print('exists')
else: 
    os.mkdir("output")

#with open(fileName, "rb") as in_file, open("out.csv", "wb") as out_file:
with open(fileName, "rb") as in_file, open(f'output\{fileName}', "wb") as out_file:
    out_file.write(in_file.read())
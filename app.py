from pathlib import Path

# Two types of Paths: 
#Absolute - Starts from the start of the harddisk
# C:\User\Sagar Shah\Program Files 
#Relative - Starts from the current working directory

#If no argument is given to the 'Path()' then the current working folder is taken 
#and we can navigate anywhere in the current folder using the pathLib library
path = Path()


#To see if a directory exists or not....!!!
#path = Path('ecommerce')
#print(path.exists())

#To create a Directory use mkdir()
#path = Path('emails')
#print(path.mkdir())

#To remove a directory
#path.rmdir()

#for file in path.glob('*.*'):
for file in path.glob('*'):
    print(file)
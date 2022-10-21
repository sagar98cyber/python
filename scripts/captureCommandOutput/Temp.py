import os


#retval = os.system('cd ..\..\\') 
retval = os.system('py command-python.py') 
print(retval)

result = os.getcwd()
print(result)
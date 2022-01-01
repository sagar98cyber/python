#importing the SYSMODULE LIBRARY
import sys

#print('Hello World!')
#sys.exit()          #The Program ends here
#print('After the SysExit!!')

#PATH shows the value of the PYTHONPATH env variable set in the current system
#print(sys.path)             #prints the path where python modules are searched

#PLATFORM function shows the Host Operating system
#print(sys.platform)         #prints the OS Name

#EXECUTABLE specifies the path of  python executable file
#print(sys.executable)       #prints python executable  file

#MODULES shows the list of all the available modules
#print(sys.modules)           #prints all modules

#COPYRIGHT shows the copyright info if PYTHON
#print(sys.copyright)

#ARGV takes the arguments at the run time stores it and executes it during the runtime
#Ctrl-Click this URL
# https://youtu.be/K3pgL2Oy3Jc?t=498
for item in sys.argv:
    print(item)

#for more sys properties visit
# https://docs.python.org/3/library/sys.html
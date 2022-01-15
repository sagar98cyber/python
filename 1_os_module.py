#https://www.youtube.com/watch?v=HHviSDUTtUc&t=23s
import os

#print(dir(os))  #dir()  - DIR FUNCTION returns all the methods and attributes of the given object

print(os.getcwd())      #printing the current working Directory
os.chdir('D://')        #changing the current working Directory
#when we change the current working directory and then if we try importing a file then python will look for that in the changed CWD 
#not in the previous one. This is why we use CHDIR
print(os.getcwd())      

#for example there is a text.txt in the current directory but since we changed the present cwd we won't be able to find that file
#f = open('test.txt').read()
#print(f)

#print(os.listdir())         #looks and displays all the files in the current directory
#print(os.listdir('D://'))   #looks and displays all the files in the D:// directory

#os.mkdir('This')
#os.rmdir('This')

#creating multiple or for creating subdirectories
#os.makedirs('This/that')   

#renaming a certain directory
#os.rename('This','this')   

#getting the envoirnment variable
#print(os.environ.get('Path'))      

#Check if an OS path exists or not
#print(os.path.exists('C:/python'))

#Check if an OS path is a file or not
#print(os.path.isfile('D:/python/India.txt'))
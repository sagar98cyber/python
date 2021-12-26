#if the input anything apart from expected input the program may crash due to invalid input
#to handle such anomilities of input and crashes we use TRY-EXCEPT BLOCKS

#for example entering a string input to 
#age = int(input('Enter your age: )) 
#gives a ValueError flag
#           ValueError: invalid literal for int() with base 10: 'sad'       -(The error we get when we enter 'sad' as the input)


#Hence we use the TRY-EXCEPT to deal with such errors
#try entering 'sad' as an input for the below code
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('You entered an invalid Value!!')
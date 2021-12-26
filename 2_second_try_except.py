#try:
#    age = int(input('Age: '))
#    income  = 20000
#    risk = income/age
#    print(age)
#except ValueError:
#    print('You entered an invalid Value!!')

#Try giving '0' as an input to the above code 
#ZeroDivisionError: division by zero                    -(The error that you get for the above code - ZeroDivisionError)
#In this case you add a ZeroDivisionError exception block

try:
    age = int(input('Age: '))
    income  = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be Zero')
except ValueError:
    print('You entered an invalid Value!!')

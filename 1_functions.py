#First function in python Greeeting a User
def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!!')

print('Start!!')
print()
#positional arguments or positional parameters
greet_user('Sagar','Shah')
#keywords arguments or keywords parameters
greet_user(last_name='Jadav',first_name='Nidhi')
print()
print('Finish!!')
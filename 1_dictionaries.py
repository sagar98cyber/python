customers = {
    'name':'John Smith',
    'age':30,
    'is_verified':True,
}

print(customers['name'])
print(customers.get('age'))
print(customers.get('birthdate'))

#we can also provide a default value
#for example if that dictionary does not have a birthdate we can provide a default birthdate
#print(customers.get('birthdate','Jan 1 1996'))


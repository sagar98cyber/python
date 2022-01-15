#declaring an integer in python
x = int(3)

#declaring an integer in python
y = float(3)

#declaring an integer in python
z = str('String')

print(x,y,z)

#declaring Dictionaries in python
Dict = {'Dict1': {1: 'Sagar',2: 'Sagar',},
        'Dict2': {'Name': 'Tushar'}}
 
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

#dictionary Functions
copy=Dict.copy()
print(f'Dictionary Copy: {copy}')
Dict.clear()
print(f'Dictionary Dict: {Dict}')
print(copy.get('Dict1').get(1))
copy.pop('Dict1')
print(copy)
print(copy.values())

#creating tuples
thistuple = ("abc", 34, True, 40, "male",34)

#tuple functions
print(len(thistuple))
print(thistuple.count(34))
print(thistuple.index(34))

#List Functions
numbers = [5,2,7,1,8,6,4]

#INSERT function
numbers.insert(4,int(input('Enter the element to be inserted: ')))
print(f'After inserting the item in the list: {numbers}')

to_be_removed = int(input('Entered the index of the item to be removed: '))
removed = False
for item in numbers:
    if item == to_be_removed:
        removed = True
        #REMOVE FUNCTION
        numbers.remove(to_be_removed)
        print(f'After removing the item in the list: {numbers}')
if removed != True:
    print('Cannot find the item that needs to be removed!!')

#REVERSE FUNCTION
numbers.reverse()
print(f'After reversing the item in the list: {numbers}')

#POP FUNCTION - REMOVING THE LAST ITEM IN THE LIST
numbers.pop()
print(f'After popping the item in the list: {numbers}')

#SORT METHOD IN LIST
numbers.sort()
print(f'After sorting the items in the list: {numbers}')
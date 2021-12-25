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

#CHECK IS CERTAIN VALUE EXISTS IN THE LIST
check_existence = int(input(f'Check if some value exists in the list: '))
if check_existence in numbers:
    print(f'The value {check_existence} exists in the Numbers List!!')
else:
    print(f'The value {check_existence} does not exist in the Numbers List!!')

#CHECK THE OCCURENCE OF A VALUE IN A LIST - USING A COUNT METHOD
check_occurence_count = int(input(f'Check the occurence of some value in the list: '))
print(f'The occurence of {check_occurence_count} in Numbers list is: {numbers.count(check_occurence_count)}')

#SORT METHOD IN LIST
numbers.sort()
print(f'After sorting the items in the list: {numbers}')
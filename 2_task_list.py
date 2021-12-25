#find the largest number in the list
limit = int(input('Enter the limit of list of numbers to be added: '))
print(limit)
numbers_list = []
items = 0
#METHOD ONE USING A WHILE LOOP, METHOD TWO USING A FOR LOOP
#while items <limit:
#    print(items)
#    numbers_list.append(int(input('Enter the number to be saved in the list: ')))
#    items+=1
#print(f'The entered list is: {numbers_list}')
#largest = numbers_list[0]

for items in range(0,limit):
    print(items)
    numbers_list.append(int(input('Enter the number to be saved in the list: ')))
    items+=1

print(f'The entered list is: {numbers_list}')
largest = numbers_list[0]

for item in numbers_list:
    if item>largest:
        largest = item
    
print(f'Largest number in the list: {largest}')
#for every entered number write the following respective numbers for it
limit = int(input('Enter the limit of list: '))
list_numbers = []
count = 0
char_list = []

while count<limit:
    list_numbers.append(int(input('Enter the number to be inserted: ')))
    count+=1

for item in list_numbers:
    if item == 1:
        char_list.append('One')
    elif item == 2:
        char_list.append('Two')
    elif item == 3:
        char_list.append('Three')
    elif item == 4:
        char_list.append('Four')
    elif item == 5:
        char_list.append('Five')
    elif item == 6:
        char_list.append('Six')
    elif item == 7:
        char_list.append('Seven')
    elif item == 8:
        char_list.append('Eight')
    elif item == 9:
        char_list.append('Nine')
    else:
        char_list.append('Zero')
    
print(f'After Converting your list the result is: {char_list}')
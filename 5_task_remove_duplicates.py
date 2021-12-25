#WRITE A PROGRAM TO REMOVE DUPLICATES FROM THE LIST
list_values = []
limit = int(input(f'Enter the number of items you want to enter in the list: '))
uniques = []
count=0

while count < limit:
    list_values.append(int(input(f'Enter the item to be entered: ')))
    count+=1

for value in list_values:
    if value not in uniques:
        uniques.append(value) 

print(f'After removing the values from the list: {uniques}')
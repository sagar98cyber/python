def accept_the_list_inputs(upper_limit):
    numbers_list = []
    count =0
    while count < upper_limit:
        numbers_list.append(int(input(f'Enter the number to be stored in the list: ')))
        count+=1
    return numbers_list



def find_the_largest_in_list(list_of_values):
    largest = 0
    for each in list_of_values:
        if largest < each:
            largest = each
    return largest
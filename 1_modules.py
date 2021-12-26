#The supporting modules file name is UTILS

#We use comparison operators to find the largest numbers and write a big long program 

#Task is to break down that whole program and create reusable functions in the UTILS file using the concepts of MODULES

#So to write a function in Utils that accepts the array finds the largest of them all!! We return them back and print it!!
import utils
from utils import find_the_largest_in_list

limit = int(input(f'Enter the upper limit of the list: '))
list_of_inputs = utils.accept_the_list_inputs(upper_limit=limit)
largest_number = find_the_largest_in_list(list_of_inputs)

print(largest_number)
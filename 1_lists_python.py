#https://www.geeksforgeeks.org/python-list/


# Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
#Lists need not be homogeneous always which makes it the most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. 
#Lists are mutable, and hence, they can be altered even after their creation.

#List in Python are ordered and have a definite count. The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. 
#Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.

# Creating a List
List = []
print("Blank List: ")
print(List)
 
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 
# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])
 
#printing a basic list
thislist = ["apple", "banana", "cherry"]
print(thislist) 

#List allows reduntant enteries
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)

#len funcition to print the length of the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
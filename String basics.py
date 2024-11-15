#len() built-in function can be used to find the length of a string (and any other sequence type) 
print(len('apple'))

#access a character at a specific index by appending brackets [ ] containing the index
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25])

#add new characters to the end of a string in a process known as string concatenation

string_1 = 'rio'
string_2 = 'schwio'
concatenated_string = string_1 + string_2
print('My pup is named ' + concatenated_string)

#list is a container created by surrounding a sequence of variables or literals with brackets [ ]; A list item is called an element 
pups = ['Rio', 'Pippy', 3] 
print(pups)

rio = 3
pippy = 6
clari = 25
home = [rio, pippy, clari]

print('rio:', home[0], 'big')
print('pippy:', home[1], 'little')
print('clari:', home[2], 'me')

#lists are mutable, meaning that they can be changed
my_nums = [5, 12, 20]
print(my_nums)

my_nums[1] = -28
print(my_nums)

#Adding elements to a list: list.append(value): Adds value to the end of list. Ex: 
my_list.append('abc')

#Removing elements from a list: list.pop(i): Removes the element at index i from list. Ex: 
my_list.pop(1)

#list.remove(v): Removes the first element whose value is v. Ex: 

my_list.remove('abc')

#tuple: behaves similar to a list but is immutable
pup = (5, 15, 20)
print(pup)

Car = NamedTuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer)
print(chevy_impala)

#Sets don’t allow duplications, and they are unordered. So they might appear in any order when you print them. Sets are useful for keeping only unique items.

animals = set(["cat", "dog", "cat", "bird"])
print(animals)

# Create a set with some items
fruits = {"apple", "banana", "cherry", "date"}

# Use pop to remove an item
removed_fruit = fruits.pop()
print("Removed:", removed_fruit)
print("Remaining fruits:", fruits)

#A dict object is created using curly braces { } to surround the key: value pairs that comprise the dictionary contents. Ex: 
pups= {'Rio': 10, 'Pippy': 7}
#Input a List Using the Map Function
add = input("1,2,3,4,5")

list = list (map (int, add.split()))
print(list)

#Basic List Comprehension
num = '1234567899'
for n in range(0,11):
    squared = [int(n)**2 for n in num]
print(squared)

#Basic List Comprehension
string = ["1", "2", "hello", "4"]

strings = [item for item in string if not item.isdigit()]

print(strings)

#Advanced List Comprehension
given = ["hello", "world"]

result = [item[::-1] for item in given]

print(result)

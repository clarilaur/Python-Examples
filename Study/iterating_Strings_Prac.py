#Iterating Through a String
def count_vowels(s):
    total = 0
    for char in s:
        if char in 'aeiou':
            total += 1
    return total
result = count_vowels('iiiiii')

print(result)

#Iterating Through a String
string = input('Insert:')

for char in string:
    print(char)

#Iterating Through a String with Index and Value
def find_char_positions(s):

    for i, char in enumerate(s):
        print(f'Index: {char}:{i}')
result = find_char_positions('apple')
print(result)

#Iterating Through a String with Index and Value
def find_char_positions(s, char):
    list = []
    index = 0

    for c in s:
        if c == char:
            list.append(index)
        index += 1
    return list
result = find_char_positions('aaleaaaa','a')
print(result)

 # Iterate over each character in the string, convert it to int, and sum the digits
def sum_digits(nums):
    added = sum(int(digit) for digit in nums)
    return added


nums = input('Insert:')

result = sum_digits(nums)

print(result)

#Write a program that takes a string input (e.g., "42") and converts it to an integer. Add 10 to the integer and print the result.
nums = input('Insert:')
number = int(nums)
added = number + 10
print(added)

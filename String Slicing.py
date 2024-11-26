#Ex: this reads the character at index 5 of the string my_str. Indices start at 0, so index 5 is a reference to the 6th character in the string.
my_str #string name
my_str[5] 

#slice notation:
my_str[start:end]

#ex: my_str is 'Boggle', then this yields string 'Bog'
my_str[0:3]

#Specifying a start index beyond the end of the string, or beyond the end index (like 3:2), yields an empty string
my_str[2:1]

#A field width is defined in a format specification by including an integer after the colon, as in {name:16} to specify a width of 16 characters
{name:16}

#fill character is used to pad a replacement field when the string being inserted is smaller than the field width. The default fill character is an empty space 
' '

#may define a different fill character in a format specification by placing the different fill character before the alignment character. ex.
{score:0>4} generates "0009" if score is 9 or "0250" if score is 250.

#find(x): Recall that in a string, the index of the first character is 0, not 1. If `my_str` is 'Boo Hoo!':
- `my_str.find('!') # Returns 7`
- `my_str.find('Boo') # Returns 0`
- `my_str.find('oo') # Returns 1 (first occurrence only)`

#find(x, start) -- Same as find(x), but begins the search at index start:
my_str.find('oo', 2) # Returns 5

#find(x, start, end) -- Same as find(x, start), but stops the search at index end - 1:
my_str.find('oo', 2, 4) # Returns -1 (not found)

#rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string

#count(x) -- Returns the number of times x occurs in the string.
- `my_str.count('oo') # Returns 2`

#String objects may be compared using relational operators:
(<, <=, >, >=), equality operators (==, !=), membership operators (in, not in), and identity operators (is, is not)

#splits the string literal "Martin Luther King Jr." using any whitespace character as the default separator and returns the list of tokens ['Martin', 'Luther', 'King', 'Jr.']
'Martin Luther King Jr.'.split()

#separator can be changed by calling split() with a string argument. Ex: uses the "#" separator to split the string "a#b#c" into the three tokens ['a', 'b', 'c']
'a#b#c'.split('#')

#join() method assigns my_str with the string 'billgates@microsoft'
my_str = '@'.join(['billgates', 'microsoft'])

#of the join() method is to build a new string without separators. The empty string ('') is a perfectly valid string object, just with a length of 0. So this statement produces the string 'http://www.ebay.com'
''.join(['http://', 'www.', 'ebay', '.com'])

#Practice 1: Access Letters
word = "Python"
print(word[0])  # First letter
print(word[-1])  # Last letter (negative indexing)

#Practice 2: Slice Strings
sentence = "Python is fun"
print(sentence[0:6])  # Output: Python
print(sentence[7:9])  # Output: is

#Practice 3: Modify Strings
text = "coding is cool"
print(text.upper())  # Output: CODING IS COOL
print(text.replace("cool", "awesome"))  # Output: coding is awesome

4. 10.1 String slicing- this is simple compared to the previous stuff lmfao
1. Strings

[10.1 String slicing](https://www.notion.so/10-1-String-slicing-12ab4a75897680cd8ae5f9ee6f6f17db?pvs=21)

user_input = input()

if user_input.isdigit():
print("Yes")
else:
print("No")

full_name = input().split()
first_name = full_name[0]

if len(full_name) == 3:
middle_name = full_name[1]
last_name = full_name[2]
print(f"{last_name}, {first_name[0]}.{middle_name[0]}.")
elif len(full_name) == 2:
last_name = full_name[1]
print(f"{last_name}, {first_name[0]}.")
else:
print("Invalid input format.")

input_string = input().split(" ", 1)
character = input_string[0]
phrase = input_string[1]

count = phrase.count(character)

if count == 1:
print(f"{count} {character}")
else:
print(f"{count} {character}'s")

while True:
item, number = input().split()
number = int(number)

```
if item == "quit":
    break

print(f"Eating {number} {item} a day keeps the doctor away.")

```

input_string = input()
cleaned_string = ''.join([char for char in input_string if char.isalpha()])
print(cleaned_string)

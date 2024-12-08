#Warm up: Parsing strings

print('Enter input string:')
name= (input())

#Report an error if the input string does not contain a comma. Continue to prompt until a valid string is entered. 
#Note: If the input contains a comma, then assume that the input also contains two strings. 
while ',' not in name:
     print('Error: No comma in string.\n')
     print('Enter input string:')
     name= (input())
else:
    print('First word: ',end='')
#Using string splitting, extract the two words from the input string and then remove any spaces. 
#Output the two words.

cutfirst = name[:4]
cutlast = name[5::]

print(cutfirst)

print ('Second word:', end='')
print(cutlast)

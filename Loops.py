#loop is a program construct that repeatedly executes the loop's statements (known as the loop body) while the loop's expression is true; when false, execution proceeds past the loop. Each time through a loop's statements is called an iteration

#while loop is a construct that repeatedly executes an indented block of code (known as the loop body) as long as the loop's expression is True

#An infinite loop is a loop that will always execute because the loop's expression is always True. A common error is to accidentally create an infinite loop by assuming equality will be reached

#The randint() function provides a new random number each time the function is called

# Iterating N times using a loop variablei = 1
while i <= N:
# Loop body statements go herei = i + 1

i = 5
while i >= 1:
# Loop body statements go here* i = i - 1
  
#The loop body executes when i is 5, 4, 3, 2, and 1, but does not execute when i reaches 0.

i = 0
while i < N:
# Loop body statements go here    i += 1

#Ex. for loop assigns the loop variable with a dictionary's keys
channels = {
  'MTV': 35,
  'CNN': 28,
  'FOX': 11,
  'NBC': 4,
  'CBS': 12
}

for c in channels:
  print(f'{c} is on channel {channels[c]}')

#ex. Using a for loop to access each character of a string.
my_str = ''
for character in "Take me to the moon.":
      my_str += character + '_'
print(my_str)

#Ex. Using a for loop over a sequence in reverse
names = [
  'Biffle',
  'Bowyer', 
  'Busch',
  'Gordon',
  'Patrick'
]

for name in names:
  print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
  print(name, '|', end=' ')
#While loops are commonly used for counting a specific number of iterations, and for loops are commonly used to iterate over all elements of a container. The range() function allows counting in for loops as well. range() generates a sequence of integers between a starting integer that is included in the range, an ending integer that is not included in the range, and an integer step value.
range(Y)
range(X, Y)
range(X, Y, Z)
range(X, Y, Z)


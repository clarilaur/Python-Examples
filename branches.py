#branch is a sequence of statements only executed under a certain condition

#***if-else*** branch has two branches: The first branch is executed IF an expression is true, ELSE the other branch is executed.Ex:

if a user inputs an age less than 25, the statement `insurePrice = 4800` executes. Else, `insurePrice = 2200` executes.

#multi branch if else example:

  num_years = int(input('Enter number years married: '))

  if num_years == 1:
      print('Your first year -- great!')
  elif num_years == 10:
      print('A whole decade -- impressive.')
  elif num_years == 25:
      print('Your silver anniversary -- enjoy.')
  elif num_years == 50:
      print('Your golden anniversary -- amazing.')
  else:
      print('Nothing special.')

#**If-elseif-else branches** programmer wishes to take one of multiple (three or more) branches. An if-else can be extended to an if-elseif-else structure. Each branch's expression is checked in sequence; as soon as one branch's expression is found to be true, that branch is taken. If no expression is found true, execution will reach the else branch, which then executes.

#equality operator (==) evaluates to true if the left and right sides are equal, and false otherwise.
  numYears = 50
  numYears == 50
#Inequality operator (!=) evaluates to true if the left and right
#Boolean is a type that has just two values: True or False
#**If-else statement** An ***if-else*** statement executes one group of statements when an expression is true, and another group of statements when the expression is false. Ex. the if-else statement outputs if a number entered by the user is even or odd. The if statement executes if divRemainder is equal to 0, and the else statement executes if divRemainder is not equal to 0.

#operator chaining is a way to combine multiple relational expressions into a single expression. The expression is true if all of the expressions are
a < b < c

my_bool = True   # Assigns my_bool with the boolean value True

is_small = 4 < 3  # Assigns is_small with the result of the expression 4 < 3 (False)

#**Multiple distinct if statements** Sometimes the programmer has multiple if statements in sequence, which looks similar to a multi-branch if-else statement but has a very different meaning. Each if statement is independent, and thus more than one branch can execute, in contrast to the multi-branch if-else arrangement.

#**Nested if-else statements** A branch's statements can include any valid statements, including another if-else statement, which are known as ***nested if-else*** statements.

# in and not in operators, known as membership operators, yield True or False if the left operand matches the value of some element in the right operand, which is always a container. EX: Use the "in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')


Enter name to check: Messi
Found Messi on the roster.
...
Enter name to check: Rooney
Could not find Rooney on the roster.

#Membership operators can be used to check whether a string is a substring, or matching subset of characters, of a larger string. For example, 'abc' in '123abcd' returns True because the substring abc exists in the larger string.
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')


#Membership in a dictionary implies that a specific key exists in the dictionary. A common error is to assume that a membership operator checks the values of each dictionary key as well. example:

my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check valuesif 3 in my_dict:
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')
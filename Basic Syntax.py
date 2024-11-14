print('Hello!, end=""')
print('Testing 123')

#Here is the output for printing a variable: 
apple = 'red'
print(apple)

#example of a string literal- can have single or double quotes
print("Hello, World!")
#adding end to print on same line but a different space
print('Hello', end=' ')
#A new variable is created by performing an assignment using the = symbol 
salary = wage * hours * weeks
#variables can be printed without quotes like this:
print(salary)
#newline charater prints everything out in a new line:
print('1\n2\n3')
#An empty print() can be used to print only a newline; Any space, tab, or newline is called whitespace.*
#Reading input is achieved using the input() function: input() reads in a string from the user, and then my_var is assigned with that string
best_friend = input()
#identifier, also called a name, is a sequence of letters (a-z, A-Z), underscores (_), and digits (0–9), and must start with a letter or an underscore:
x = 5
r = 1234
apple = 346
#syntax for outputting the float myFloat with two digits after the decimal; F point/Expression Evaluation: Inside the f-string, any code enclosed in curly braces {} will be evaluated as a Python expression before being inserted into the string. Formatting: The :.2f part is a format specifier that controls how the expression inside the curly braces is formatted.
print(f'{myFloat:.2f}')

#You use import math to make these mathematical functions and constants available for you to use in your code- ex:
import math

print(f'{math.pi:.4f}')

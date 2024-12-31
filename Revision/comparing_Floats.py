import math
one = float(input())
two = float(input())
epsilon = float(input())

difference = abs(one - two)


if difference < 0.001: 
    print("equal")
elif difference < epsilon: 
    print("close enough")
else: 
    print("not close")  

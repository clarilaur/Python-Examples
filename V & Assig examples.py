#example 4
import math

f0 = float(input())

r = math.pow(2, 1/12)

f1 = f0 * math.pow(r, 1)
f2 = f0 * math.pow(r, 2)
f3 = f0 * math.pow(r, 3)

print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')

#example 3
import math

x = float(input())
y = float(input())
z = float(input())

var1 = x ** z
var2 = x ** (y ** z)
var3 = abs(x - y)
var4 = math.sqrt(x ** z)

print(f'{var1:.2f} {var2:.2f} {var3:.2f} {var4:.2f}')

#example 2
age = int(input())
weight = float(input())
heart_rate = int(input())
time = float(input())

calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

print(f'Calories: {calories:.2f} calories')

#example 1- floor division means being able to do this stuff:

user_num = int(input())
div_num = int(input())

#Perform floor division three times

result1 = user_num // div_num
result2 = result1 // div_num
result3 = result2 // div_num

print(result1, result2, result3)
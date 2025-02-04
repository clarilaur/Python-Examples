import math

num = int(input())

if num > 0:
    result = math.sqrt(num)
if num < 0:
    result = math.fabs(num)
else:  
    result = 0
print(result)

i = int(input())

make = [] 

while i > 0:
    make.append(i)  
    increment = int(input()) 
    i = increment  
    if i == 0:
        break
# Check if the list is empty before finding min and max
smallest = min(make)
largest = max(make)
print(f'{smallest} and {largest}')

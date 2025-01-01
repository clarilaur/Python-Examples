num_integers = int(input())

numbers = []
for _ in range(num_integers):
    numbers.append(int(input()))  

threshold = int(input()) 

result = [str(num) + ',' for num in numbers if num <= threshold]

print(''.join(result), end='')

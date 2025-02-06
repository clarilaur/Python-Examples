num = int(input())
first = num // 1000000
third = num % 10000
second = str(num)[3:5]

print(f'{first}-{second}-{third}')

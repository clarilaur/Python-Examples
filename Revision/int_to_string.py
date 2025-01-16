num = int(input())

one = num // 1000000
three = num % 10000

num_str = str(num)

# Get the 3rd and 4th index (0-based indexing)
second = num_str[3:5]

print(f'{one}-{second}-{three}')

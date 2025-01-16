user_values = []   # List of integers from input

n = int(input().strip())

for value in range(n-1):
    user_values.append(int(input().strip()))
final = int(input().strip())

user_values.insert(0,final)

print(' '.join(map(str, user_values))+ ' ')

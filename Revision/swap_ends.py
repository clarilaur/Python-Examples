user_values = list(map(int, input().split()))

first_value = user_values[0]
last_value = user_values[-1]

user_values[0] = last_value
user_values[-1] = first_value

print(' '.join(map(str, user_values)) + ' ')

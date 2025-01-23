parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    except ValueError:
        print(f'{name} 0')
    parts = input().split()
    name = parts[0]

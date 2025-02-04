filename = 'quotes.txt'

with open(filename, 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total += 1
        print(f'Line {total}:{line.strip()}')

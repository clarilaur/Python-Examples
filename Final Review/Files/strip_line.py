filename = 'dogs.txt'

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        cleaned = line.strip()
        print(cleaned)

filename = 'animals.txt'

with open(filename, 'r') as file:
    lines = file.readlines()

with open('uppercase_animals.txt', 'w') as upperfile:
    for line in lines:
        upper = line.strip().upper()
        upperfile.write(upper)
with open('uppercase_animals.txt', 'r') as upperfile:
    context = upperfile.read()
    print(context)

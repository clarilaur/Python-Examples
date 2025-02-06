import csv

filename = 'numbers.csv'
pairs = {}

with open(filename, 'r') as file:
    filelist = csv.reader(file)

    # Read the first (and only) line and split by commas
    for row in filelist:
        numbers = map(int, row)  # Convert each value to an integer
        for num in numbers:
            pairs[num] = pairs.get(num, 0) + 1  # Count occurrences

# Sort dictionary by keys and print results
for num in sorted(pairs.keys()):
    print(num, pairs[num])

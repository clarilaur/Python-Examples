import csv

filename = input()
dict1 = {}
dict2 = {}
with open(filename, 'r') as file:
    rows = csv.reader(file)
    rows = list(rows)
    if len(rows) == 2:
        for row in rows:
#study these two lines
            dict1 = {rows[0][i].strip(): rows[0][i + 1].strip() for i in range(0, len(rows[0]), 2)} 
            dict2 = {rows[1][i].strip(): rows[1][i + 1].strip() for i in range(0, len(rows[1]), 2)}
        print(dict1)
        print(dict2)

one = input()
two = input()

match = 0
min_length = min(len(one), len(two))

for i in range(min_length): 
    if one[i] == two[i]:
        match += 1

if match == 1:
    print(f'{match} character matches')
else:
    print(f'{match} characters match')

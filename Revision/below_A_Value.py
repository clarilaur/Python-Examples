string = list(input().split())

threshold = int(string[-1])

output = []

for value in string[:-1]:
    if int(value) <= threshold:
        output.append(value)
        
print(','.join(output) + ',')

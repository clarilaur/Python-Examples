predef_list = [4, -27, 15, 33, -10]

digit = int(input())

split = predef_list

maxval = max(split)

if digit > maxval: 
    print(f'Greater Than Max? True')
else: 
    print(f'Greater Than Max? False')

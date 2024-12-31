num = int(input())

digits = len(str(num))

if 0 < num <= 9:
    print(f'{digits} digit')
elif num == 0:
    print('1 digit')
else:
    print(f'{digits} digits')

time = input()
age= int(input())

if age in [3,2,1,0]:
    price = "free"
    print(f'{price}')
elif time == "day" and 4 <= age:
    price = 8
    print(f'${price}')
elif time == "night":
    if age in range(17,55):
        price = 15
    elif age in range(4,17):
        price = 12
    else:
        price = 13
    print(f'${price}')

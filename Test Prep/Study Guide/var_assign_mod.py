ton = 2000 *16
pound = 16 * 1

ounces = int(input())

value_1 = ounces // ton
remainder = ounces % ton
value_2 = remainder// pound
remainder = remainder % pound
value_3 = remainder


print(f'Tons: {value_1}')
print(f'Pounds: {value_2}')
print(f'Ounces: {value_3}')

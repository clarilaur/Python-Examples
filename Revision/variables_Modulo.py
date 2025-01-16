integer = int(input())

remainder = 0

value_1 = integer//32000
leftover = integer % 32000
remainder = leftover

value_2 = leftover//16
leftover2 = leftover%16
remainder=leftover2

value_3 = remainder

print(f'Tons: {value_1}')
print(f'Pounds: {value_2}')
print(f'Ounces: {value_3}')

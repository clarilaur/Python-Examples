totalChangeAmount = int(input())

total = totalChangeAmount
dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

total = totalChangeAmount
num_dollars = total // 100
total -= num_dollars * 100
num_quarters = total // 25
total -= num_quarters * 25
num_dimes = total // 10
total -= num_dimes * 10
num_nickels = total // 5
total -= num_nickels * 5
num_pennies = total // 1
total -= num_pennies * 1

if totalChangeAmount <= 0:
    print('No change')
if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1: 
        print('Dollar')
    else:
        print('Dollars')
if num_quarters > 0:
    print(num_quarters, end=' ')
    if num_quarters == 1: 
        print('Quarter')
    else:
        print('Quarters')
if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1: 
        print('Dime')
    else:
        print('Dimes')
if num_nickels > 0:
    print(num_nickels, end=' ')
    if num_nickels == 1: 
        print('Nickel')
    else:
        print('Nickels')
if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1: 
        print('Penny')
    else:
        print('Pennies')

def exact_change(user_total):
    total = user_total
    num_quarters = total // 25
    total -= num_quarters * 25
    num_dimes = total // 10
    total -= num_dimes * 10
    num_nickels = total // 5
    total -= num_nickels * 5
    num_pennies = total // 1
    total -= num_pennies * 1
    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__': 
    input_val = int(input())    
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    # Type your code here.
    if input_val <= 0:
        print('no change')
    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1: 
            print('penny')
        else:
            print('pennies')
    if num_nickels > 0:
        print(num_nickels, end=' ')
        if num_nickels == 1: 
            print('nickel')
        else:
            print('nickels')
    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1: 
            print('dime')
        else:
            print('dimes')
    if num_quarters > 0:
        print(num_quarters, end=' ')
        if num_quarters == 1: 
            print('quarter')
        else:
            print('quarters')

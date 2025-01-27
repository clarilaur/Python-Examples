def count_evens(num1, num2, num3, num4):
    total = 0
    for item in num1, num2, num3, num4:
        if item % 2 == 0:
            total += 1
        if item % 2 == 1:
            total += 0
    return total
if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    
    result = count_evens(num1, num2, num3, num4)
    print('Total evens:', result)

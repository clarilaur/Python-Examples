names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    findindex = names[index]
    print(f'Name: {findindex}')
    
except IndexError:
    print('Exception! list index out of range')
    
    if index < 0:
        print(f'The closest name is: {names[0]}')
    elif index > 0:
        print(f'The closest name is: {names[-1]}')

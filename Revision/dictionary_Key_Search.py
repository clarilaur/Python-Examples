stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

amount = int(input())

total = 0

for _ in range(amount):
    stockoptions= input().strip()
    if stockoptions in stocks:
        total += stocks[stockoptions]
print(f'Total price: ${total}')

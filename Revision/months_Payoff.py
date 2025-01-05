loan_amount = float(input())
payment_amount = float(input())
interest_rate = float(input())


balance = loan_amount
payments = 0

while balance > 0:

    balance += balance * interest_rate
    
    balance -= payment_amount
    payments += 1
    
    if balance < 0:
        balance = 0

if payments == 1:
    print(f"{payments} payment")
else:
    print(f"{payments} payments")

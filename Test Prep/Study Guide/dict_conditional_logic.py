purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase
item = input()
amount = int(input())

if item in purchase:
    price = purchase[item]*amount

if amount < 10:
    print(price)
    print(f"{item} ${price:.2f}")
if 10 <= amount <= 20:
    price = price * 0.95
    print(f"{item} ${price:.2f}")
if 21 <= amount:
    price = price * 0.90
    print(f"{item} ${price:.2f}")

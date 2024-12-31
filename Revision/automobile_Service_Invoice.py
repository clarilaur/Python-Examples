print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()
print('Select first service:')
firstservice = input()
print('Select second service:')
secondservice = input()
print()
if firstservice == "Oil change":
    firstprice = 35
elif firstservice == "Tire rotation":
    firstprice = 19
elif firstservice == "Car wash":
    firstprice = 7
elif firstservice == "Car wax":
    firstprice = 12
else: 
    print('-')
    
if secondservice == "Oil change":
    secondprice = 35
elif secondservice == "Tire rotation":
    secondprice = 19
elif secondservice == "Car wash":
    secondprice = 7
elif secondservice == "Car wax":
    secondprice = 12
else: 
    print('-')


print("Davy's auto shop invoice")
print()
print(f"Service 1: {firstservice}, ${firstprice}")
print(f"Service 2: {secondservice}, ${secondprice}")
print()
total = firstprice+secondprice
print(f"Total: ${total}")

amountrequired = area/350 

print(f"Paint needed: {amountrequired:.3f} gallons")

cans = int(math.ceil(amountrequired))

print(f'Cans needed: {cans} can(s)')
#Total cost includes paint and sales tax.

paintcost = cost_paint_can*float(cans)
salestax = float(paintcost)*.07
total = salestax+paintcost

print(f'Paint cost: ${paintcost:.2f}')
print(f'Sales tax: ${salestax:.2f}')
print(f'Total cost: ${total:.2f}')

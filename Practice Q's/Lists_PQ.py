# Prompt for four weights. Add all weights to a list. Output list.
weight1 = float(input())
weight2 = float(input())
weight3 = float(input())
weight4 = float(input())

print('Enter weight 1:')
print('Enter weight 2:')
print('Enter weight 3:')
print('Enter weight 4:')
makelist = [weight1,weight2,weight3,weight4]
print('Weights:', makelist)
print()
# Output average of weights.

average = sum(makelist) / len(makelist)
print(f"Average weight: {average:.2f}")
# Output max weight from list.

maxlist = max(makelist)
print(f"Max weight: {maxlist:.2f}")

onelist= list(map(int,input().split()))
twolist= list(map(int,input().split()))

total = 0

for one, two in zip(onelist, twolist):
    result = one*two
    total += result

print(total)

items = [1, 4.8, 7, 9.2, 3, 6]

print(items[3])
print(items[-1])

newitems = items[1:4]
print(newitems)
diffitems = items[1:]
print(diffitems)
thriftitems = items[:4]
print(thriftitems)

matchitems = 1 in items
print(matchitems)
nomatchitems = 1 not in items
print(nomatchitems)

print(len(items))
print(max(items))
print(min(items))
print(sorted(items)) #smallest to largest
print(sorted(items, reverse=True)) #largest to smallest
print(sum(items))

names = ['Rio', 'Pippy', 'Clari']
name1 = names.append('Jenny')
print(names)

name2 = names.pop() #last item on list
name3 = names.pop(1) #first item on list
listjoined = ", ".join(names)

print('Welcome to the club ' + listjoined, '!')

#RUNDOWN ON SETS:
apple = set()
v = apple.add(1,2,3)
d = apple.discard(2,3)
print(list(names))
print(set(items))

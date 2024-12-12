#while loops

temp = 34

while temp >= 32:
    print(temp)
    temp-= 1
print('it is freezing')

#ranges

sum = 0

for num in range(1,5): #runs loops for numbers 1 through 4, because range is exclusive of the ending position
    sum += num
print(sum)

i = 0
for i in range(1,10):
    print(i)
    i = i + 1
print('done')

#for loops:

cities = ['New York','Los Angeles','Chicago','Houston']
for city in cities:
    print('Welcome to the city of {}'.format(city))

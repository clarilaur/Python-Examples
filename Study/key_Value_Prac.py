#Basic Key-Value Storage Using Split
apple = "name=John"

app = apple.split('=')

key, value = app

dic = {key:value}

print(dic)

#Handling Split Output
receive = "key1:value1,key2:value2,key3:value3"

split = receive.split(',')
dict = {}
for item in split:
    separate = item.split(':')
    key, value = separate
    dict[key] = value
print(dict)

#Basic Dictionary Reversal
receive = {"a": 1, "b": 2, "c": 3}

dict = {}
for key, value in receive.items():

    dict[value]= key
print(dict)

#Reversing Dictionary with Conditions
receive = {"a": 1, "b": 2, "c": 3}

dict = {value:key for key, value in receive.items() if value > 1}

print(dict)

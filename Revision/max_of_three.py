one = int(input())
two = int(input())
three = int(input())

if one==two==three:
    print(one)
elif one > two and one > three:
    print(one)
elif two > one and two > three:
    print(two)
else: 
    print(three)

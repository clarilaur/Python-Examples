#Basic Multiple Variable Assignment

def swap_values(a, b):
    one = a
    two = b

    a = two
    b = one
    return a, b
result = swap_values('a', 'b')
print(result)

#Unpacking
given = ['1','2']

x, y = given

print(x)
print(y)

red = int(input())
green = int(input())
blue = int(input())

findgray = min(red,green,blue)

calcgray = [(red-findgray),(green-findgray),(blue-findgray)]

print(calcgray[0],calcgray[1], calcgray[2])

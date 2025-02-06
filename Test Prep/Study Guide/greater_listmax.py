predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list

num = int(input())

greatest = max(predef_list)

boo = num > greatest

print(f'Greater Than Max? {boo}')

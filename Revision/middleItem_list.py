integers = input()

nums = []
for value in integers.split():
    nums.append(int(value))

middle = len(nums)//2

print(nums[middle])

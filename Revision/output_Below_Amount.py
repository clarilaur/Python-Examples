# Define your get_user_values function here
def get_user_values(nums): 
    while True:
        value = int(input().strip())
        if value == -1:
            break
        nums.append(value)
# Define your output_ints_less_than_or_equal_to_threshold function here
def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    for value in nums:
        if value <= threshold:
            print(value)

if __name__ == '__main__':
    threshold = int(input())
    nums = []
    
    get_user_values(nums)
    output_ints_less_than_or_equal_to_threshold(nums, threshold)

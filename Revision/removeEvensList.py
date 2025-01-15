def remove_evens(nums):
    result = [num for num in nums if num % 2 != 0]
    return result


    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_evens(nums)
    
    print(result)

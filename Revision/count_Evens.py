def count_evens(nums):
    counter = 0
    for n in nums:
        if n % 2 == 0:  
            counter += 1  
    return counter

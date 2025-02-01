def calc_average(nums):
    total = sum(nums)  # Calculate the sum of the list
    average = total / len(nums)  # Divide by the number of elements
    return float(average)


if __name__ == '__main__':
    nums = input("Enter numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]  # Convert input to a list of integers
    print(calc_average(nums))

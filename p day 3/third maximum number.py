def third_maximum(nums):

    nums = list(set(nums))

    if len(nums) < 3:
        return max(nums) 

    nums.sort(reverse=True)
    return nums[2]

numbers = [7, 2, 3, 5, 6, 1, 4, 7, 6]
result = third_maximum(numbers)
print(f"The third maximum number is: {result}")

def max_subarray(nums):
    max_current = max_global = nums[0]
    
    for x in nums[1:]:
        max_current = max(x, max_current + x)

        max_global = max(max_global, max_current)
    
    return max_global

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray(nums)
print(f"Maximum subarray sum: {max_sum}")

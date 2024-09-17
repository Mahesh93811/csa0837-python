def moveZeroes(nums):
   
    last_non_zero_found_at = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  

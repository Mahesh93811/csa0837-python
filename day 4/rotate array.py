def rotate(nums, k):
    n = len(nums)
    k = k % n 

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)

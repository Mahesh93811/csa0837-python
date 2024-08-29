def subsets(nums):
    result = [[]] 
    
    for num in nums:
        new_subsets = [curr + [num] for curr in result]
        result.extend(new_subsets)
    
    return result

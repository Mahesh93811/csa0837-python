def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)

    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        mid1, mid2 = merged[n // 2 - 1], merged[n // 2]
        return (mid1 + mid2) / 2 
nums1 = [1, 3]
nums2 = [2]
print("Median:", find_median_sorted_arrays(nums1, nums2)) 
def find_first_last(arr, target):
    def binary_search_left(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    first_pos = binary_search_left(arr, target)
    last_pos = binary_search_right(arr, target)
    if first_pos <= last_pos:
        return [first_pos, last_pos]
    else:
        return [-1, -1]
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = find_first_last(arr, target)
print("First and Last Position of target:", result)

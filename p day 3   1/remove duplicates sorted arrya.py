def remove_duplicates(arr):
    if not arr:
        return 0

    unique_index = 0
    for i in range(1, len(arr)):

        if arr[i] != arr[unique_index]:

            unique_index += 1
            arr[unique_index] = arr[i]
    return unique_index + 1

arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)

print(f"Array after removing duplicates: {arr[:length]}")
print(f"Length of array after removing duplicates: {length}")

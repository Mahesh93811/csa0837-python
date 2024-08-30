def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = is_sorted(my_list)
print(result)  # Output will be True

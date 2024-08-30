def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# Example usage:
my_list = [1, 2, 3, 4, 5, 1]
result = has_duplicates(my_list)
print(result)  # Output will be True

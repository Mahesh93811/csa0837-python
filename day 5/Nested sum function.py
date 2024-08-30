def nested_sum(nested_lst):
    total = 0
    for sublist in nested_lst:
        total += sum(sublist)
    return total

# Example usage:
my_list = [[1, 2, 3], [4, 5], [6]]
result = nested_sum(my_list)
print(result)  # Output will be 21

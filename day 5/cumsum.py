def cumsum(numbers):
    cumsum_list = []
    total = 0
    for num in numbers:
        total += num
        cumsum_list.append(total)
    return cumsum_list

# Example usage:
my_list = [1, 2, 3, 4]
result = cumsum(my_list)
print(result)  # Output will be [1, 3, 6, 10]

def are_triangular(a, b, c):
    # Check if each side is less than the sum of the other two sides
    return (a < b + c) and (b < a + c) and (c < a + b)

# Example usage:
print(are_triangular(3, 4, 5))  # True
print(are_triangular(10, 1, 1)) # False
print(are_triangular(6, 8, 10)) # True
print(are_triangular(1, 2, 3))  # False

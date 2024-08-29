def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)   
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle)))
n = 5  
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)
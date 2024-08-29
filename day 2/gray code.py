def gray_code(n):
    result = []
    for i in range(2 ** n):
        result.append(i ^ (i >> 1))
    return result


n = 3
print(gray_code(n))

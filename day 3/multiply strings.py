def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)

    num1, num2 = num1[::-1], num2[::-1]

    for i in range(len1):
        for j in range(len2):
            result[i + j] += int(num1[i]) * int(num2[j])
            result[i + j + 1] += result[i + j] // 10 
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(map(str, result[::-1]))
num1 = "123"
num2 = "456"
print(multiply_strings(num1, num2))

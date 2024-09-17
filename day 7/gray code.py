def generate_gray_code(n):
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0", "1"]

    prev_gray_code = generate_gray_code(n - 1)

    first_half = ['0' + code for code in prev_gray_code]

    second_half = ['1' + code for code in reversed(prev_gray_code)]

    return first_half + second_half

n = 3
gray_code_sequence = generate_gray_code(n)
print(gray_code_sequence)

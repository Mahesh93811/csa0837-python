binary_digits = []
for i in range(4):
    while True:
        digit = input(f"Enter binary digit {i+1}: ")
        if digit in ['0', '1']:
            binary_digits.append(digit)
            break
        else:
            print("Invalid input. Please enter 0 or 1.")

binary_number = ''.join(binary_digits)
decimal_equivalent = int(binary_number, 2)
print(f"The decimal equivalent of the binary number {binary_number} is {decimal_equivalent}.")
def divide_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result:.2f}.")
    else:
        print("Error: Division by zero is not allowed.")

divide_numbers()
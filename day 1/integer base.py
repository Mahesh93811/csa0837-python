def calculate_power(base, exponent):
    """
    Calculate the value of base raised to the power of exponent.

    Args:
        base (int): The base number.
        exponent (int): The exponent.

    Returns:
        int: The result of base raised to the power of exponent.
    """
    return base ** exponent

def main():
   
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    
    result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")

if __name__ == "__main__":
    main()
 def display_powers_of_two(n):
    """
    This function displays the powers of 2 from 2^0 to 2^n.
    
    Args:
        n (int): The highest power of 2 to display.
    """
    for i in range(n + 1):
        print(f"2^{i} = {2 ** i}")


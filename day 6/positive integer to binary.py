def int_to_binary(n):
    """
    Convert a positive integer to its binary representation.

    Args:
        n (int): A positive integer.

    Returns:
        str: The binary representation of n as a string.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    s = ""
    while n > 0:
       
        s = str(n % 2) + s
       
        n = n // 2

    return s

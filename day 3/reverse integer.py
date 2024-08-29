def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    reversed_n = int(str(n)[::-1])
  
    return sign * reversed_n

number = 12345
reversed_number = reverse_integer(number)
print(f"Reversed integer: {reversed_number}")
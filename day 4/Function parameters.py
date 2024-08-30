def is_power(a, b):
    if a == 1:
        return True
    
    
    if b == 1 or a % b != 0:
        return False
    
    
    return is_power(a // b, b)


print(is_power(8, 2)) 
print(is_power(27, 3)) 
print(is_power(10, 2)) 
print(is_power(1, 10)) 
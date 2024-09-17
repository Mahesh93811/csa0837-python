def is_perfect_square(num):
    if num < 0:
        return False  
    
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False


num = 16
print(is_perfect_square(num))  

num = 14
print(is_perfect_square(num))  

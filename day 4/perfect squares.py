import math

def is_perfect_square(num):
    if num < 0:
        return False
    root = int(math.sqrt(num))
    return root * root == num

num = 16
print(is_perfect_square(num)) 

num = 20
print(is_perfect_square(num)) 
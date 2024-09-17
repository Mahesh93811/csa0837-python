def isPowerOfFour(num: int) -> bool:
    if num <= 0:
        return False
    while num % 4 == 0:
        num //= 4
    return num == 1

print(isPowerOfFour(16)) 
print(isPowerOfFour(15)) 
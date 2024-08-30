def find_complement(num: int) -> int:
    if num == 0:
        return 1
    
    num_bits = num.bit_length()

    bitmask = (1 << num_bits) - 1
    
  
    return num ^ bitmask

num = 5
print(find_complement(num))

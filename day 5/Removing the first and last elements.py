def chop(lst):
    if len(lst) > 1:
        lst.pop(0)  
        lst.pop(-1)  
    elif len(lst) == 1:
        lst.pop()  
   
    return None

# Example usage:
my_list = [1, 2, 3, 4]
chop(my_list)
print(my_list)  # Output will be [2, 3]

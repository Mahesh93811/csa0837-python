def first_unique_char(s):

    freq_dict = {}
     
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    
    for char in s:
        if freq_dict[char] == 1:
            return char


print(first_unique_char("harshith"))
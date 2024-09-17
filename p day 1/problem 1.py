def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    i, j = 0, len(s) - 1
    s = [char for char in s]  # Convert string to a list without using list()

    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            # Swap the vowels manually
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

    # Manually combine characters back into a string
    result = ''
    for char in s:
        result += char
    
    return result

# Example usage:
print(reverse_vowels("hello"))  # Output: "holle"
print(reverse_vowels("leetcode"))  # Output: "leotcede"
  
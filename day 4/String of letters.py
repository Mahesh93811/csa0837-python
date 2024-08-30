def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

# Example usage:
print(uses_only("hello", "helo"))   # True
print(uses_only("world", "helo"))   # False
print(uses_only("apple", "aepl"))   # True

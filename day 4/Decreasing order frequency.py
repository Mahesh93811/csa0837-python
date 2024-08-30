def most_frequent(s):
    # Create a dictionary to count the frequency of each character
    frequency = {}
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
    
    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the letters in decreasing order of frequency
    for char, freq in sorted_frequency:
        print(f"{char}: {freq}")

# Example usage:
most_frequent("banana")

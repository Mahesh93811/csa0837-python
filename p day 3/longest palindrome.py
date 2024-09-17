def longest_palindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) == 0:
        return ""

    longest = ""
    for i in range(len(s)):

        palindrome_odd = expand_around_center(i, i)
        palindrome_even = expand_around_center(i, i + 1)

        longest = max(longest, palindrome_odd, palindrome_even, key=len)

    return longest
input_string = "babad"
print("Longest palindrome is:", longest_palindrome(input_string))

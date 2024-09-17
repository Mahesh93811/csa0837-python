def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def partition(s: str):
    result = []
    part = []

    def dfs(start):
        if start >= len(s):
            result.append(part[:])
            return
        
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            if is_palindrome(substring):
                part.append(substring)
                dfs(end + 1)
                part.pop()

    dfs(0)
    return result

s = "aab"
partitions = partition(s)
print(partitions)

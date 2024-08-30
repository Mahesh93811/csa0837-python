def integer_break(n: int) -> int:
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    
    return dp[n]

n = 10
print(integer_break(n)) 

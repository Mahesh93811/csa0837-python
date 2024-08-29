def is_interleave(A, B, C):
    if len(A) + len(B) != len(C):
        return False
    dp = [[False] * (len(B) + 1) for _ in range(len(A) + 1)]

    dp[0][0] = True

    for i in range(1, len(A) + 1):
        dp[i][0] = dp[i-1][0] and A[i-1] == C[i-1]

    for j in range(1, len(B) + 1):
        dp[0][j] = dp[0][j-1] and B[j-1] == C[j-1]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            dp[i][j] = (dp[i-1][j] and A[i-1] == C[i+j-1]) or (dp[i][j-1] and B[j-1] == C[i+j-1])

    return dp[len(A)][len(B)]

A = "abc"
B = "def"
C = "adbcef"
result = is_interleave(A, B, C)
print(f"Is '{C}' an interleaving of '{A}' and '{B}'? {result}")

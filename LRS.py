def longest_repeating_subsequence(S):
    n = len(S)
    dp = [[0] * (n+1) for _ in range(n+1)]

   
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

   
    i, j = n, n
    lrs = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + 1 and S[i-1] == S[j-1] and i != j:
            lrs.append(S[i-1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    lrs.reverse()
    return "".join(lrs)


S = "AABCBDC"
result = longest_repeating_subsequence(S)
print("Longest Repeating Subsequence:", result)
print("Length of LRS :",len(result))

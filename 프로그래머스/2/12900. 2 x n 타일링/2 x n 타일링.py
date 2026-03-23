def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, len(dp)):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007
    
    return dp[-1] % 1_000_000_007
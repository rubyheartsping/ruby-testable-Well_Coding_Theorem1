N = int(input())
dp = [0] * (N + 1)
if N >= 2:
    dp[1], dp[2] = 1, 2
    for i in range(3, len(dp)):
        dp[i] = dp[i - 2] + dp[i - 1]
else:
    dp[1] = 1

print(dp[N] % 10007)

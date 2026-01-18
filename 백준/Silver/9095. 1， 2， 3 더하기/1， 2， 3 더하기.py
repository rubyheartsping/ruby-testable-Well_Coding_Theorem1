import sys
input = sys.stdin.readline

T = int(input().rstrip("\n"))
numbers = [int(input().rstrip("\n")) for t in range(T)]

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for t in range(4, max(numbers) + 1):
    dp[t] = dp[t - 1] + dp[t - 2] + dp[t - 3]

for number in numbers:
    print(dp[number])

def solution(money):
    if len(money) <= 3:
        return max(money)
    money1 = money[1:]
    money2 = money[:-1]
    
    def circular_dp(money: list):
        dp = [0] * len(money)
        dp[0] = money[0]
        dp[1] = max(money[0], money[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
        return dp[-1]
    
    return max(circular_dp(money1), circular_dp(money2))
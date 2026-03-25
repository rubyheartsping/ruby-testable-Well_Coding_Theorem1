def solution(sticker):
    
    if len(sticker) <= 3:
        return max(sticker)
    
    sticker1 = sticker[:-1]
    sticker2 = sticker[1:]
    
    def DP(sticker: list):
        dp = [0] * len(sticker)
        dp[0] = sticker[0]
        dp[1] = max(sticker[0], sticker[1])
        for i in range(2, len(sticker)):
            dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
        
        return max(dp[-1], dp[-2])
        
    return max(DP(sticker1), DP(sticker2))
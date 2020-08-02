class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[1] > 1: return False
        n = len(stones)
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        dp[0][0] = True
        for i in range(n):
            for j in range(i):
                k = stones[i] - stones[j]
                if k <= i:
                    dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
        return any(dp[-1])
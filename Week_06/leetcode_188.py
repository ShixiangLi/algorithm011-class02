class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        else:
            dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n + 1)]
            for i in range(k + 1):
                dp[0][i][1] = float('-inf')
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
            return dp[-1][-1][0]
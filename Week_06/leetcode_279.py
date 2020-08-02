class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1: return 1
        value = int(math.sqrt(n))
        values = [i ** 2 for i in range(1, value + 1)]
        dp = [n + 1 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in values:
                if j > i: break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]
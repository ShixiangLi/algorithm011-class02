class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins: return 1 if amount == 0 else 0
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin > i : continue
                dp[i] = dp[i] + dp[i - coin]
        return dp[-1]
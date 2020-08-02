class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp_i_10, dp_i_11 = 0, float('-inf')
        dp_i_20, dp_i_21 = 0, float('-inf')
        for i in range(n):
            dp_i_20 = max(dp_i_20, dp_i_21 + prices[i])
            dp_i_21 = max(dp_i_21, dp_i_10 - prices[i])
            dp_i_10 = max(dp_i_10, dp_i_11 + prices[i])
            dp_i_11 = max(dp_i_11, -prices[i])
        return dp_i_20
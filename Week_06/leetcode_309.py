class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp_i_pre, dp_i_0, dp_i_1 = 0, 0, float('-inf')
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_pre - prices[i])
            dp_i_pre = temp
        return dp_i_0
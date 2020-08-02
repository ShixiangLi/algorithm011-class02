class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return None
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        n = len(nums)
        def myrob(arr):
            n = len(arr)
            dp = [0 for _ in range(n + 1)]
            dp[1] = arr[0]
            for i in range(2, n + 1):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + arr[i - 1]
                )
            return dp[-1]
        return max(myrob(nums[1:]), myrob(nums[:n - 1]))
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        n = len(nums)
        min_value = max_value = nums[0]
        res = nums[0]
        for i in range(1, n):
            temp = max_value
            max_value = max(max_value * nums[i], min_value * nums[i], nums[i])
            min_value = min(min_value * nums[i], temp * nums[i], nums[i])
            res = max(res, max_value)
        return res
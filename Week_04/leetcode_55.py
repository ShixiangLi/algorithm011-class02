class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        endable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= endable:
                endable = i
        return endable == 0
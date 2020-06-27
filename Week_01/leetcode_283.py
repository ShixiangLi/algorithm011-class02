class Solution:
    def moveZeroes(self, nums):
        # 双指针
        # 时间复杂度：O(N)
        # 空间复杂度：O(1)
        if not nums or len(nums) == 0:
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


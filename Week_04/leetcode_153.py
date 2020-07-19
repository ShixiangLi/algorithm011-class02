class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
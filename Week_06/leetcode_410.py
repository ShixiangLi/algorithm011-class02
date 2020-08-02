class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums or not m: return -1
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if self.group(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left
    def group(self, nums, mid):
        count, values = 1, 0
        for num in nums:
            if values + num > mid:
                values = num
                count += 1
            else:
                values += num
        return count
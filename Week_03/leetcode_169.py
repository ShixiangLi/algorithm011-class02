class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        candidate = None
        count = 0
        for num in nums:
            if not count:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
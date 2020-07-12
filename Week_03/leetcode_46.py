class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        return self.backtrack(nums, [], [])

    def backtrack(self, nums, track, res):
        if not nums:
            res.append(track[:])
            return res
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], track + [nums[i]], res)
        return res
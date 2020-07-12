class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        for i in range(len(nums) + 1):
            self.backtrack(nums, 0, i, [], res)
        return res

    def backtrack(self, nums, start, k, track, res):
        if k == len(track):
            res.append(track)
            return
        for i in range(start, len(nums) - (k - len(track) - 1)):
            self.backtrack(nums, i + 1, k, track + [nums[i]], res)
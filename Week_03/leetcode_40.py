class Solution:
    def combinationSum2(self, candidates, target):
        # 回溯
        # 时间复杂度：O(N*N!)
        # 空间复杂度：O(N*N!)
        if not candidates: return []
        candidates.sort()
        return self.backtrack(candidates, 0, [], target, [])

    def backtrack(self, nums, start, track, target, res):
        if target == 0:
            res.append(track[:])
            return res
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums, i + 1, track + [nums[i]], target - nums[i], res)
        return res
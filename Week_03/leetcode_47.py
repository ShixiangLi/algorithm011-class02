class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        visited = [False for _ in range(len(nums))]
        nums.sort()
        return self.backtrack(nums, visited, [], [])
    def backtrack(self, nums, visited, track, res):
        if len(track) == len(nums):
            res.append(track[:])
            return res
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                self.backtrack(nums, visited, track + [nums[i]], res)
                visited[i] = False
        return res
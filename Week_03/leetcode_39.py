class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, [], target, res)
        return res

    def backtrack(self, candidates, start, track, target, res):
        if target == 0:
            res.append(track[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            self.backtrack(candidates, i, track + [candidates[i]], target - candidates[i], res)
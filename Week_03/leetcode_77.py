class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n: return []
        return self.backtrack(n, k, 1, [], [])

    def backtrack(self, n, k, start, track, res):
        if k == len(track):
            res.append(track[:])
            return res
        for i in range(start, n + 1 - (k - len(track) - 1)):
            self.backtrack(n, k, i + 1, track + [i], res)
        return res
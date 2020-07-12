class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        return self.backtrack(n, n, '', [])

    def backtrack(self, left, right, track, res):
        if left == 0 and right == 0:
            res.append(track)
            return res
        if left > 0:
            self.backtrack(left - 1, right, track + '(', res)
        if right > left:
            self.backtrack(left, right - 1, track + ')', res)
        return res


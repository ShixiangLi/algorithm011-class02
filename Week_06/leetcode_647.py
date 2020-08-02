class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        n = len(s)
        self.res = 0
        for i in range(n):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
        return self.res

    def helper(self, s, left, right):
        i = left
        j = right
        while 0 <= i and j < len(s):
            if s[i] == s[j]:
                self.res += 1
                i -= 1
                j += 1
            else:
                break
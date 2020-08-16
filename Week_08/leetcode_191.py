class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        res = 0
        while n != 0:
            res += 1
            n = n & (n - 1)
        return res
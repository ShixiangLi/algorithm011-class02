class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 31
        while n:
            res += (n & 1) << count
            n >>= 1
            count -= 1
        return res
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        cur = x
        while x / cur < cur:
            cur = (cur + x / cur) // 2
        return int(cur)
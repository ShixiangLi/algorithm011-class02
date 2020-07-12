class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n == 1: return x
        if n < 0:
            n = -n
            x = 1 / x
        y = self.myPow(x, n // 2)
        return y * y if n % 2 == 0 else y * y * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        while n:
            if n & 1:
                res = x * res
            x *= x
            n //= 2
        return res
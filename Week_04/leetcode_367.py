class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * mid >= num:
                right = mid - 1
            else:
                left = mid + 1
        return left * left == num
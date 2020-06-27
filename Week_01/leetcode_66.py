class Solution:
    def plusOne_1(self, digits):
        # 倒序遍历
        # 时间复杂度：O(N)
        # 空间复杂度：O(1)
        if not digits or len(digits) == 0:
            return []
        count = 1
        for i in range(len(digits) - 1, -1, -1):
            cur = digits[i] + count
            count = cur // 10
            digits[i] = cur % 10
            if count == 0:
                return digits
        digits = [1] + digits
        return digits

    def plusOne_2(self, digits):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if digits == []:
            return [1]
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            return self.plusOne_2(digits[:-1]) + [0]
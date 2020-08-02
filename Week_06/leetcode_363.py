class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return None
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            rowSum = [0 for _ in range(m)]
            for right in range(left, n):
                for r in range(m):
                    rowSum[r] += matrix[r][right]
                res = max(res, self.helper(rowSum, k))
                if res == k: return res
        return res

    def helper(self, arr, k):
        nums = arr[:]
        for i in range(1, len(nums)):
            nums[i] = max(0, nums[i - 1]) + nums[i]
        if max(nums) <= k: return max(nums)

        res = float('-inf')
        for l in range(len(arr)):
            for r in range(l, len(arr)):
                cur = sum(arr[l:r + 1])
                if cur <= k:
                    res = max(res, cur)
                    if res == k: return res
        return res
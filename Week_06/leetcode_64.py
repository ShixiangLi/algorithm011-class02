class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return None
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            cur = grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
            return cur

        return dp(m - 1, n - 1)
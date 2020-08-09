class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        directVec = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
        queue = deque()
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        elif n <= 2:
            return n

        queue.append((0, 0, 1))
        grid[0][0] = 1
        while queue:
            i, j, step = queue.popleft()
            for dx, dy in directVec:
                if i + dx == n - 1 and j + dy == n - 1:
                    return step + 1
                if 0 <= i + dx <= n - 1 and 0 <= j + dy <= n - 1 and grid[i + dx][j + dy] == 0:
                    queue.append((i + dx, j + dy, step + 1))
                    grid[i + dx][j + dy] = 1
        return -1

        from collections import deque
        directVec = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        queue = deque()
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        elif n <= 2:
            return n
        queue.append((0, 0, 1))
        grid[0][0] = 1
        while queue:
            i, j, step = queue.popleft()
            for dx, dy in directVec:
                if i + dx == n - 1 and j + dy == n - 1:
                    return step + 1
                if 0 <= i + dx <= n - 1 and 0 <= j + dy <= n - 1 and grid[i + dx][j + dy] == 0:
                    queue.append((i + dx, j + dy, step + 1))
                    grid[i + dx][j + dy] = 1
        return -1


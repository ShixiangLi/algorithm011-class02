class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.count = n
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parents[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        else:
            self.parents[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        self.count -= 1
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    def counter(self):
        return self.count
    def connected(self, p, q):
        return self.find(p) == self.find(p)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1)]
        land = UnionFind(m * n + 1)
        water = m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in directions:
                        row = i + dx
                        col = j + dy
                        if row < m and col < n and grid[row][col] == '1':
                            land.union(i * n + j, row * n + col)
                else:
                    land.union(water, i * n + j)
        return land.counter() - 1


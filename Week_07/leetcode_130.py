class UnionFind:
    def __init__(self, capacity):
        self.parents = [i for i in range(capacity)]
        self.rank = [1 for _ in range(capacity)]
        self.count = capacity
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
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
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        dummy = m * n
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        uf.union(i * n + j, dummy)
                    else:
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            x, y = i + dx, j + dy
                            if board[x][y] == 'O':
                                uf.union(i * n + j, x * n + y)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and uf.find(dummy) != uf.find(i * n + j):
                    board[i][j] = 'X'
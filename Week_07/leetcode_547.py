class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        visited = set()
        n = len(M)
        res = 0

        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
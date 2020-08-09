class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        root = {}
        end_of_word = '#'
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[end_of_word] = end_of_word

        self.res = set()
        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, '', root)
        return list(self.res)

    def dfs(self, board, row, col, track, node):
        track += board[row][col]
        node = node[board[row][col]]
        if '#' in node:
            self.res.add(track)
            # return
        board[row][col], temp = '@', board[row][col]
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = row + i, col + j
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in node:
                self.dfs(board, x, y, track, node)
        board[row][col] = temp
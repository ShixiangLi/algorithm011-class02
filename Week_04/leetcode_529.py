class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        queue = collections.deque()
        queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            count = self.counter(board, r, c)

            if count != 0:
                board[r][c] = str(count)
                continue

            board[r][c] = 'B'
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0: continue
                    new_row = r + i
                    new_col = c + j
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'E':
                        queue.append((new_row, new_col))
                        board[new_row][new_col] = 'B'
        return board

    def counter(self, board, row, col):
        res = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0: continue
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'M':
                    res += 1
        return res
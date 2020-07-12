class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        up = set()
        up_left = set()
        up_right = set()
        return self.backtrack(board, up, up_left, up_right, 0, [])

    def backtrack(self, board, up, up_left, up_right, row, res):
        if row == len(board):
            res.append(self.buildres(board))
            return res
        for col in range(len(board[0])):
            if col in up or row + col in up_left or row - col in up_right:
                continue
            board[row][col] = 'Q'
            up.add(col)
            up_left.add(row + col)
            up_right.add(row - col)
            self.backtrack(board, up, up_left, up_right, row + 1, res)
            board[row][col] = '.'
            up.remove(col)
            up_left.remove(row + col)
            up_right.remove(row - col)
        return res

    def buildres(self, board):
        res = []
        for i in range(len(board)):
            res.append(''.join(board[i]))
        return res
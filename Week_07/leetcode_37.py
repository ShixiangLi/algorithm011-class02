class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return

        def isValid(x, y, s):
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True


        def backtrack(index):
            if index == 81:
                return True
            x, y = index // 9, index % 9
            if board[x][y] != '.':
                return backtrack(index + 1)
            for i in range(1, 10):
                s = str(i)
                if isValid(x, y, s):
                    board[x][y] = s
                    if backtrack(index + 1):
                        return True
                    board[x][y] = '.'
            return False

        backtrack(0)
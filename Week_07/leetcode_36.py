class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if cur in rows[i] or cur in cols[j] or cur in boxes[i // 3 * 3 + j // 3]:
                        return False
                    rows[i].append(cur)
                    cols[j].append(cur)
                    boxes[i // 3 * 3 + j // 3].append(cur)
        return True
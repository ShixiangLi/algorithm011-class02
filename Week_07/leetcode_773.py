from collections import deque


class Solution:
    def slidingPuzzle(self, board):
        m, n = 2, 3
        start = []
        target = [1, 2, 3, 4, 5, 0]

        for i in range(m):
            for j in range(n):
                start.append(board[i][j])

        neighbor = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2]
        ]

        q = deque()
        visited = []
        q.appendleft(start)
        visited.append(start)
        step = 0

        while q:
            size = len(q)
            for i in range(size):
                cur = q.pop()
                if cur == target:
                    return step
                index = cur.index(0)
                for adj in neighbor[index]:
                    new_board = cur.copy()
                    new_board[index], new_board[adj] = new_board[adj], new_board[index]
                    if new_board not in visited:
                        q.appendleft(new_board)
                        visited.append(new_board)
            step += 1
        return -1
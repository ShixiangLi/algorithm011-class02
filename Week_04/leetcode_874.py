class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands: return 0
        res = 0
        obstacles = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col, d = 0, 0, 0
        for cmd in commands:
            if cmd == -2:
                d = (d - 1 + 4) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = directions[d]
                for i in range(cmd):
                    new_x = row + dx
                    new_y = col + dy
                    if (new_x, new_y) in obstacles: break
                    row, col = new_x, new_y
                    res = max(res, row ** 2 + col ** 2)
        return res
from collections import deque
class Solution(object):
    def levelOrder_1(self, root):
        # 迭代
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not root:
            return []
        cur_level = deque()
        cur_level.appendleft(root)
        res = []
        while cur_level:
            next_level = deque()
            temp = []
            while cur_level:
                node = cur_level.pop()
                temp.append(node.val)
                for n in node.children:
                    if n:
                        next_level.appendleft(n)
            res.append(temp)
            cur_level = next_level
        return res

    def levelOrder_2(self, root):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = []

        def level(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            for node in root.children:
                level(node, depth + 1)

        level(root, 0)
        return res
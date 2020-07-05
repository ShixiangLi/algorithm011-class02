class Solution(object):
    def postorder_1(self, root):
        # 迭代
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                if child:
                    stack.append(child)
        return res[::-1]

    def postorder_2(self, root):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = []
        def post(root):
            if not root:
                return []
            for node in root.children:
                post(node)
            res.append(root.val)

        post(root)
        return res
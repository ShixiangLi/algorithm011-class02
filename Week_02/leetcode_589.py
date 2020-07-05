class Solution(object):
    def preorder_1(self, root):
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
            for child in node.children[::-1]:
                if child:
                    stack.append(child)
        return res

    def preorder_2(self, root):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = []
        def pre(root):
            if not root:
                return []
            res.append(root.val)
            for node in root.children:
                pre(node)


        pre(root)
        return res
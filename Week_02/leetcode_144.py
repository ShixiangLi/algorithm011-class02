class Solution:
    def preorderTraversal_1(self, root):
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
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversal_2(self, root):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = []
        def preorder(root):
            if not root:
                return []
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
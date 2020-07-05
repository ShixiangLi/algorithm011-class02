class Solution:
    def inorderTraversal_1(self, root):
        # 迭代
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not root:
            return []
        stack = []
        node_p = root
        res = []
        while stack or node_p:
            while node_p:
                stack.append(node_p)
                node_p = node_p.left
            node_p = stack.pop()
            res.append(node_p.val)
            node_p = node_p.right
        return res

    def inorderTraversal_2(self, root):
        # 递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = []
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

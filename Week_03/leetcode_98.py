class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res == sorted(res) and len(res) == len(set(res))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lower, higher):
            if not root: return True
            if root.val <= lower or root.val >= higher:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, higher)
        return helper(root, float('-inf'), float('inf'))
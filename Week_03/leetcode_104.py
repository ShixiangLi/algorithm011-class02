class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                res = max(res, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return res

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return (min(left_depth, right_depth) or max(left_depth, right_depth)) + 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root, 1)]
        res = float('inf')
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                res = min(res, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return res
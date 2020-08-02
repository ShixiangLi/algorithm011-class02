# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        @functools.lru_cache(None)
        def myrob(root):
            if not root: return [0, 0]
            left_trees = myrob(root.left)
            right_trees = myrob(root.right)
            do = root.val + left_trees[0] + right_trees[0]
            not_do = max(left_trees) + max(right_trees)
            return [not_do, do]
        return max(myrob(root))
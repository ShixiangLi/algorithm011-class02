class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        hash_map = {root: None}

        def dfs(root):
            stack = [root]
            while stack:
                node = stack.pop()
                if node.right:
                    hash_map[node.right] = node
                    stack.append(node.right)
                if node.left:
                    hash_map[node.left] = node
                    stack.append(node.left)

        dfs(root)
        l1, l2 = p, q
        if p not in hash_map or q not in hash_map:
            return None
        while l1 != l2:
            l1 = hash_map[l1] if l1 else q
            l2 = hash_map[l2] if l2 else p
        return l1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root: return False
            if root == p or root == q: return root
            right_tree = helper(root.right, p, q)
            left_tree = helper(root.left, p, q)
            if left_tree and right_tree: return root
            return left_tree or right_tree
        return helper(root, p, q)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        stack = [root]
        index = 0
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            temp = None
            while stack and stack[-1].val == inorder[index]:
                temp = stack.pop()
                index += 1
            if temp:
                temp.right = node
            else:
                stack[-1].left = node
            stack.append(node)
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
        return root
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root):
            if not root:
                res.append(None)
                return
            rserialize(root.left)
            rserialize(root.right)
            res.append(root.val)

        res = []
        rserialize(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(data):
            if data[0] == None:
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.right = rdeserialize(data)
            root.left = rdeserialize(data)
            return root

        return rdeserialize(data[::-1])


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            rserialize(root.left)
            rserialize(root.right)

        res = []
        rserialize(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(data):
            if data[0] == None:
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = rdeserialize(data)
            root.right = rdeserialize(data)
            return root

        return rdeserialize(data)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        queue = collections.deque()
        queue.append(root)
        for i in range(1, len(data), 2):
            node = queue.popleft()
            if i == len(data) - 1:
                node.left = TreeNode(data[i])
                break
            if data[i] != None:
                node.left = TreeNode(data[i])
                queue.append(node.left)
            if data[i + 1] != None:
                node.right = TreeNode(data[i + 1])
                queue.append(node.right)
        return root
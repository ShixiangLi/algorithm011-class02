class Node:
    def __init__(self, k, v):
        self.nex = None
        self.pre = None
        self.key = k
        self.val = v


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, node):
        node.nex = self.head.nex
        self.head.nex.pre = node
        node.pre = self.head
        self.head.nex = node
        self.size += 1

    def remove(self, node):
        node.pre.nex = node.nex
        node.nex.pre = node.pre
        node.pre = None
        node.nex = None
        self.size -= 1

    def removeLast(self):
        if self.tail.pre == self.head:
            return None
        last = self.tail.pre
        self.remove(last)
        return last


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        v = self.hash_map[key].val
        self.put(key, v)
        return v

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.hash_map:
            self.cache.remove(self.hash_map[key])
            self.cache.addFirst(node)
            self.hash_map[key] = node
        else:
            if self.cap == self.cache.size:
                del self.hash_map[self.cache.removeLast().key]
            self.cache.addFirst(node)
            self.hash_map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
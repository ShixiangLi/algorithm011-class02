# 双端队列设计

# 1.平民版
# 用内置函数，复杂度高
# 没有什么算法思想
# 也没有实现循环

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.capacity = k
        self.count = 0
        self.stack = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count >= self.capacity:
            return False
        self.stack.insert(0, value)
        self.count += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count >= self.capacity:
            return False
        self.stack.append(value)
        self.count += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False
        del self.stack[0]
        self.count -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.stack.pop()
        self.count -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.stack[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.count == 0:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.count == self.capacity:
            return True
        return False

# 2.求余操作实现循环双端队列
class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:
            return False

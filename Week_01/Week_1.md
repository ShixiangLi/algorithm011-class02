# 第一周学习总结

培养复杂度分析习惯，学习数组、链表、栈、队列基本数据结构，学习调表、双端队列高级数据结构。

## 时间复杂度与空间复杂度

1. 最好时间复杂度：可以理解为最好情况下的时间复杂度，如对有序的数组排序，对平衡二叉树遍历等；
2. 最坏时间复杂度：最坏情况下的时间复杂度，如对逆序数据排序，对退化成链表的二叉树遍历等；
3. （补充）平均时间复杂度：精确计算需要利用概率论知识进行复杂度的计算，计算每种情况复杂度时要乘以相应的概率；
4. （补充）均摊时间复杂度：与平均时间复杂度类似，将最坏情况的时间均摊到其他情况，如数组插入数据。

## 数组和链表

1. 数组和链表时最基本的数据结构，所有其他的数据结构都是基于数组和链表建立的，如树是有带有左右指针的链表储存，也可以用数组对应下标储存。数组、链表属于线性结构；
2. 数组在内存中时连续的空间存储，链表由指针相连不需要连续空间。使得数组随机访问为O(1)，链表为O(N)。访问数组元素时，先找到数组头地址，根据地质偏移量和连续的特性，访问数组元素，这也是第一个索引为0的原因；
3. 数组的插入、删除为O(N)，因为涉及数据搬移，链表都是O(1)

## 栈和队列

1. 栈是后进先出，队列是先进先出；
2. python中栈和队列的主要实现功能如下
	
stack的主要API

	empty() – Returns whether the stack is empty – Time Complexity : O(1)
	size() – Returns the size of the stack – Time Complexity : O(1)
	top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
	push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
	pop() – Deletes the top most element of the stack – Time Complexity : O(1)

queue.Queue的主要API

	maxsize – Number of items allowed in the queue.
	empty() – Return True if the queue is empty, False otherwise.
	full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
	get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
	get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
	put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
	put_nowait(item) – Put an item into the queue without blocking.
	qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.

## 跳表

1. 跳表是为了给有序的链表的查询提高速度而产生的；
2. 跳表是在有序链表的基础上，增加维度，高维的节点数是低维节点数 // 2；
3. 查询过程从高维开始，逐步判断缩小区间，可以跳过一些节点，因此可以提高效率；
4. 查询的时间复杂度：O(logN)，类似二分查找。

## 优先队列

1. 结合栈和队列，为了实现让每次弹出的元素按照一定优先级的顺序弹出，我们牺牲一定的时间，原来的弹出是O(1)，优先队列是O(logN)；

2. 优先队列的简单实现：

	class PriorityQueue(object): 
	    def __init__(self): 
	        self.queue = [] 
	  
	    def __str__(self): 
	        return ' '.join([str(i) for i in self.queue]) 
	  
	    # for checking if the queue is empty 
	    def isEmpty(self): 
	        return len(self.queue) == 0
	  
	    # for inserting an element in the queue 
	    def insert(self, data): 
	        self.queue.append(data) 
	  
	    # for popping an element based on Priority 
	    def delete(self): 
	        try: 
	            max = 0
	            for i in range(len(self.queue)): 
	                if self.queue[i] > self.queue[max]: 
	                    max = i 
	            item = self.queue[max] 
	            del self.queue[max] 
	            return item 
	        except IndexError: 
	            print() 
	            exit() 


2. 堆是一种优先队列，二叉堆是一种基本的堆结构，分为大顶堆，堆顶元素为最大，父节点大于子节点。小顶堆，堆顶元素为最小，父节点小于子节点；
3. 每次弹出，插入都需要对堆进行堆化，保证堆顶元素时最大或最小；

python的heapq类主要API：

	heapq.heappush(heap, item)
	heapq.heappop(heap)
	heapq.heappushpop(heap, item)
	heapq.heapify(x)
	heapq.heapreplace(heap, item)

## 双端队列

1. 双端队列实现在队列两头都可以插入、删除

python中的deque可以实现：

	append() :- This function is used to insert the value in its argument to the right end of deque.	
	appendleft() :- This function is used to insert the value in its argument to the left end of deque.	
	pop() :- This function is used to delete an argument from the right end of deque.	
	popleft() :- This function is used to delete an argument from the left end of deque.









	

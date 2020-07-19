# Week_4

### 搜索-遍历

每个节点都要访问一次

每个节点仅仅要访问一次

对于节点的访问顺序不限
	-BFS
	-DFS
	-启发式搜索（优先级）

### 深度优先搜索

示例代码：

递归写法：

	visited = set()
	def dfs(node):
		if node in visited:
			# already visited
			return 
		visited.add(node)
		# process current node
		# ... # logic here
		dfs(root.left)
		dfs(root.right)
	# 多叉树
	def dfs(node, visited):
		visited.add(node)
		# process current node here
		...
		for next_node in node.children():
			if not next_node in visited:
				dfs(next_node, visited)
	def dfs(node, visited):
		if node in visited: # terminator
			# already visited
			return

		visited.add(node)

		# process current node here
		...
		for next_node in node.children():
			if not next_node in visited:
				dfs(next_node, visited)

迭代法，栈：

def DFS(self, tree):
	
	if tree.root is None:
		return []
	
	visited, stack = [], [tree.root]
	
	while stack:
		node = stack.pop()
		visited.add(node)

		process(node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)
	# other processing work
	...

### 广度优先遍历

代码实现：

	def BFS(graph, start, end):
		
		queue = []
		queue.append([start])
		visited.add(start)
	
		while queue:
			node = queue.popleft()
			visited.add(node)
	
			process(node)
			nodes = generate_related_nodes(node)
			queue.push(nodes)
	
		# other processing work
		...

### 贪心算法

何时适用贪心算法？

问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种字问题最优解称为最优子结构。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

### 二分查找

二分查找的前提条件：

1. 目标函数单调性（单调递增或递减）
2. 存在上下界（bounded）
3. 能够通过索引访问（index accessible）

代码模板：

	def binsearch(arr):
		
		left, right = 0, len(arr) - 1
		while left <= right:
			mid = left + ((right - left) >> 1)
			if arr[mid] == target:
				# find the target!
				break or return result
			elif arr[mid] < taqrget:
				left = mid + 1
			else:
				right = mid - 1





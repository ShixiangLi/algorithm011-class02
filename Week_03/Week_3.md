# Week_3：学习总结

### 递归

递归模板：

	def recursion(level, param1, param2, ...):
		# recursion terminator
		if level > MAX_LEVEL:
			process_result
			return 
	
		# process logic in current level
		process(level, data...)
	
		# drill down
		self.recursion(level + 1, p1, p2, ...)
	
		# reverse the current level status if needed

递归注意事项

1. 摒弃人肉递归（手动模拟递归过程，画递归树）
2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3. 数学归纳法思维

### 分治、回溯

找到重复性->分解子问题->合并子问题结果

分治模板：

	def recursion(problem, param1, param2, ...):
		# recursion terminator
		if problem is None:
			process_result
			return
		# prepare data
		data = prepare_data(problem)
		subproblems = split_problem(problem, data)
		# conquer subproblems
		subresult1 = self.divide_conquer(subproblems[0], p1, ...)
		subresult2 = self.divide_conquer(subproblems[1], p1, ...)
		subresult3 = self.divide_conquer(subproblems[2], p1, ...)
		# process and generate the final result
		result = process_result(subresult1, subresult2, subresult3, ...)
		# revert the current level states

回溯算法与泛型递归类似。
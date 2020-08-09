# Trie树
	class Trie:
		def __init__(self):
			self.root = {}
			self.end_of_word = "#"
		def insert(self, word):
			node = self.root
			for char in word:
				node = node.setdefault(char, {})
			node[self.end_of_word] = self.end_of_word
		def search(self, word):
			node = self.root
			for char in word:
				if char not in node:
					return False
				node = node[char]
			return self.end_of_word in node
		def startsWith(self, prefix):
			node = self.root
			for char in prefix:
				if char not in node:
					return False
				node = node[char]
			return True

# 并查集

### 并查集模板

	class UnionFind:
		def __init__(self, capacity):
			self.parents = [i for i in range(capacity)]
			self.count = capacity
			self.rank = [1 for _ in range(capacity)]
		def union(seld, p, q):
			root_p = self.find(p)
			root_q = self.find(q)
			if root_p == root_q: return
			if self.rank[root_p] > self.rank[root_q]:
				self.parents[root_q] = root_p
				self.rank[root_p] += self.rank[root_q]
			else:
				self.parents[root_p] = root_q
				self.rank[root_q] += self.rank[root_p]
			self.count -= 1
		def find(self, p):
			while p != self.parents[p]:
				self.parents[p] = self.parents[self.parents[p]]
				p = self.parents[p]
			return p
		def counter(self):
			return self.count
		def connected(self, p, q):
			return self.find(p) == self.find(q)

#A*启发式搜索

优先级搜索

#红黑树、AVL树

赞略
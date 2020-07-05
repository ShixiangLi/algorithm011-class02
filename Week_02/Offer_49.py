class Solution:
    def nthUglyNumber_1(self, n):
        # 动态规划
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        dp = [1 for _ in range(n)]
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]

    def nthUglyNumber_2(self, n):
        # 堆
        # 时间复杂度：O(NlogN)
        # 空间复杂度：O(N)
        heap = [1]
        for i in range(n):
            cur = heapq.heappop(heap)
            if cur * 2 not in heap:
                heapq.heappush(cur * 2)
            if cur * 3 not in heap:
                heapq.heappush(cur * 3)
            if cur * 5 not in heap:
                heapq.heappush(cur * 5)
        return cur
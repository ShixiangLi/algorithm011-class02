class Solution:
    def topKFrequent_1(self, nums, k):
        # 哈希 + 排序
        # 时间复杂度：O(N + NlogN + N)
        # 空间复杂度：O(N)
        hash_map = collections.Counter(nums)
        res = []
        temp_list = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(temp_list[0])
        return res

    def topKFrequent_2(self, nums, k):
        # 哈希 + 小顶堆
        # 时间复杂度：O(N + NlogK + N)
        # 空间复杂度：O(N)
        hash_map = collections.Counter(nums)
        res = []
        heap = []
        for num, fre in hash_map.items():
            if len(heap) == k:
                if fre > heap[0][0]:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, (fre, num))
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

    def topKFrequent_3(self, nums, k):
        # 桶排序
        # 时间复杂度：O(N + N + N)
        # 空间复杂度：O(N)
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []
        for num, fre in collections.Counter(nums).items():
            buckets[fre].append(num)
        for l in range(buckets[::-1]):
            if len(l) != 0:
                res += l
            if len(res) >= k:
                return res[:k]


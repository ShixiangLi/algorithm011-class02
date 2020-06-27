class Solution:
    def getLeastNumbers_1(self, nums, k):
        # 利用快排思想
        # 时间复杂度：O(N)
        # 空间复杂度：O(logN) 递归栈
        def partition(nums, low, high):
            if low >= high:
                return low
            pivot_index = random.randint(low, high)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        low, high = 0, n - 1
        index = partition(nums, low, high)
        while index != k:
            if index > k:
                high = index - 1
                index = partition(nums, low, high)
            else:
                low = index + 1
                index = partition(nums, low, high)
        return nums[:k]

    from heapq import *
    def getLeastNumbers_2(self, nums, k):
        # 大顶堆
        # 时间复杂度：O(NlogK)
        # 空间复杂度：O(K)
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]] # 默认小顶堆
        heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heappop(hp)
                heappush(hp, -arr[i])
        res = [-x for x in hp]
        return res
















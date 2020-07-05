class Solution:

    def heapSort(self, nums):
        if len(nums) <= 1:
            return nums
        self.buildheap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
        return nums

    def buildheap(self, data):
        n = len(data)
        for i in range((n - 2) // 2, -1, -1):
            self.heapify(data, i, n)

    def heapify(self, data, i, n):
        while True:
            maxPos = i
            if i * 2 + 1 < n and data[i] < data[i * 2 + 1]:
                maxPos = 2 * i + 1
            if i * 2 + 2 < n and data[maxPos] < data[i * 2 + 2]:
                maxPos = i * 2 + 2
            if maxPos == i:
                break
            data[i], data[maxPos] = data[maxPos], data[i]
            i = maxPos
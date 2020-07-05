class Solution:
    def twoSum_1(self, nums, target):
        # 暴力
        # 时间复杂度：O(N^2)
        # 空间复杂度：O(1)
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_2(self, nums, target):
        # 两遍哈希
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not nums or len(nums) == 0:
            return []
        hash_map = {}
        for index, num in enumerate(nums):
            hash_map[num] = index
        for index, num in enumerate(nums):
            cur = target - num
            if hash_map.get(cur) and hash_map[cur] != index:
                return [index, hash_map[cur]]
        return []

    def twoSum_3(self, nums, target):
        # 一遍哈希
        # 时间复杂度：
        # 空间复杂度：
        if not nums or len(nums) == 0:
            return []
        hash_map = {}
        for index, num in enumerate(nums):
            if hash_map.get(target - num) is not None:
                return [hash_map[target - num], index]
            hash_map[num] = index
        return []












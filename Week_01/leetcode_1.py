class Solution:
    def twoSum_1(self, nums, target):
        # 哈希表
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        hash_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [index, hash_map[diff]]
            else:
                hash_map[num] = index
        return []

    def twoSum_2(self, nums, target):
        # 双指针
        # 时间复杂度：O(nlogn + n)
        # 空间复杂度：O(N)
        nums_sort = sorted(nums)
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            cur = nums_sort[left] + nums_sort[right]
            if cur == target:
                index_1 = nums.index(nums_sort[left])
                if nums_sort[left] == nums_sort[right]:
                    index_2 = nums.index(nums_sort[right], index_1 + 1)
                    return [index_1, index_2]
                else:
                    index_2 = nums.index(nums_sort[right])
                    return [index_1, index_2]
            elif cur > target:
                right -= 1
            else:
                left += 1
        return []
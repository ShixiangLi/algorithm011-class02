class Solution:
    # 暴力
    # 时间复杂度：O(N*k)
    # 空间复杂度：O(1)
    def rotate_1(self, nums, k):
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        for i in range(k):
            for j in range(n - 1):
                nums[j], nums[n - 1] = nums[n - 1], nums[j]

    # 转置旋转
    # 时间复杂度：O(N)
    # 空间复杂度：O(1)
    def rotate_2(self, nums, k):
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # 环状旋转
    # 时间复杂度：O(N)
    # 空间复杂度：O(1)
    def rotate_3(self, nums, k):
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        start, count = 0, 0
        while count < n:
            # loop变量处理第一次cur == start进入循环
            loop = 0
            cur = start
            temp = nums[start]
            post = (cur + k) % n
            while loop == 0 or cur != start:
                nums[post], temp = temp, nums[post]
                count += 1
                cur = post
                post = (cur + k) % n
                loop += 1
            start += 1

    # 方法三的优化
    def rotate_3_sim(self, nums, k):
        count, cur, temp = 0, 0, nums[0]
        # 记录已经交换过的位置
        done_index = set()
        done_index.add(0)
        while count < len(nums):
            count, target = count + 1, (index + k) % len(nums)
            temp, nums[target] = nums[target], temp
            if target not in done_index:
                index = target
            elif target + 1 < len(nums):
                index, temp = target + 1, nums[target + 1]
            done_index.add(index)







class Solution:
    # 双指针
    # 时间复杂度：O(m + n)
    # 空间复杂度：O(1)
    def merge(self, nums1, m, nums2, n):
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]





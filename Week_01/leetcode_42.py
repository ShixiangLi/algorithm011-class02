class Solution:
    def trap_1(self, height):
        # 双指针
        # 时间复杂度：O(N)
        # 空间复杂度：O(1)
        res = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while left <= right:
            if max_left < max_right:
                res += max(max_left - height[left], 0)
                max_left = max(max_left, height[left])
                left += 1
            else:
                res += max(max_right - height[right], 0)
                max_right = max(max_right, height[right])
                right -= 1
        return res

    def trap_2(self, height):
        # 单调栈
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        res = 0
        stack = []
        cur = 0
        while cur < len(height):
            if not stack or height[stack[-1]] >= height[cur]:
                stack.append(cur)
                cur += 1
            else:
                while height[stack[-1]] < height[cur]:
                    temp = stack.pop()
                    if not stack:
                        break
                    min_height = min(height[cur], height[stack[-1]])
                    res += max(0, min_height - height[temp]) * (cur - stack[-1] - 1)
                stack.append(cur)
                cur += 1
        return res
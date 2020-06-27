class Solution:
    def largestRectangleArea_1(self, heights):
        # 单调栈
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not heights or len(heights) == 0:
            return 0
        stack = [-1]
        res = 0
        cur = 0
        while cur < len(heights):
            if stack[-1] == -1 or heights[stack[-1]] <= heights[cur]:
                stack.append(cur)
                cur += 1
            else:
                while heights[stack[-1]] > heights[cur]:
                    temp = stack.pop()
                    res = max(res, (cur - stack[-1] - 1) * heights[temp])
                    if stack[-1] == -1:
                        break
                stack.append(cur)
                cur += 1
        while stack[-1] != -1:
            temp = stack.pop()
            res = max(res, (len(heights) - stack[-1] - 1) * heights[temp])
        return res

    def largestRectangleArea_2(self, heights):
        # 别人写的精简版
        stack = []
        heights = [0] + heights + [0] # 哨兵
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[temp])
            stack.append(i)
        return res

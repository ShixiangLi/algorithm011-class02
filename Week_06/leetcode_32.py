class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        res = 0
        for i in range(2, n + 1):
            if s[i - 1] == ')':
                if s[i - 2] == '(':
                    dp[i] = 2 + dp[i - 2]
                elif s[i - 2] == ')' and i - 2 - dp[i - 1] >= 0 and s[i - 2 - dp[i - 1]] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
                res = max(res, dp[i])
        return res
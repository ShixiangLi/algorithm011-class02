class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if '10' <= s[i - 2:i] <= '26':
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 0
            else:
                if '10' <= s[i - 2:i] <= '26':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]
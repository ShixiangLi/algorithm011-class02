class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0: return 0
        dp_i_01, dp_i_10, dp_i_00 = 1, 1, 1
        dp_i_21, dp_i_20, dp_i_11 = 0, 0, 0
        for i in range(1, n):
            t01, t10, t00, t21, t20, t11 = dp_i_01, dp_i_10, dp_i_00, dp_i_21, dp_i_20, dp_i_11
            dp_i_01 = (t10 + t20 + t00) % 1000000007

            dp_i_10 = t00
            dp_i_20 = t10
            dp_i_21 = t11
            dp_i_11 = t01

            dp_i_00 = (t10 + t20 + t00) % 1000000007
            dp_i_01 += (t11 + t21 + t01) % 1000000007
        return (dp_i_00 + dp_i_01 + dp_i_21 + dp_i_10 + dp_i_11 + dp_i_20) % 1000000007
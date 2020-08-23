class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        s = list(s)

        for j in range(len(s)):
            if j == len(s) - 1:
                self.Reversechar(s, i, j + 1)

            if s[j] == ' ':
                self.Reversechar(s, i, j)
                i = j + 1

        return ''.join(s)

    def Reversechar(self, s, start, end):
        mid = start + (end - start) // 2
        l = end - 1
        for k in range(start, mid):
            s[k], s[l] = s[l], s[k]
            l -= 1
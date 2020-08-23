class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                if t[i] in dct.values():
                    return False
                dct[s[i]] = t[i]
            else:
                if dct[s[i]] != t[i]:
                    return False
        return True

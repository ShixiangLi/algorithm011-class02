class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  
        n = len(p)
        p = "".join(sorted(p))
        res = []
        for i in range(len(s) - n + 1):
            if "".join(sorted(s[i:i + n])) == p:
                res.append(i)
        return res

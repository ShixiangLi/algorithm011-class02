class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hash_map = Counter(s)
        for c in t:
            if c not in hash_map:
                return False
            else:
                hash_map[c] -= 1
                if hash_map[c] == 0:
                    del hash_map[c]
        return hash_map == {}
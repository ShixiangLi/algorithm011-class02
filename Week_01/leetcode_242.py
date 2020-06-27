class Solution:
    def isAnagram_1(self, s, t):
        # 排序
        # 时间复杂度：O(NlogN)
        # 空间复杂度：O(1)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_2(self, s, t):
        # 哈希表
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        hash_map = {}
        for ch in s:
            if ch not in hash_map:
                hash_map[ch] = 1
            else:
                hash_map[ch] += 1
        for ch in t:
            if ch not in hash_map:
                return False
            else:
                hash_map[ch] -= 1
                if hash_map[ch] == 0:
                    del hash_map[ch]
        return len(hash_map) == 0

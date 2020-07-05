class Solution:
    def groupAnagrams_1(self, strs):
        # 排序+哈希
        # 时间复杂度：O(N*KlogK) K为最大字符串长度
        # 空间复杂度：O(N)
        if not strs or len(strs) == 0:
            return []
        hash_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            hash_map[key] = hash_map.get(key, []) + [s]
        # py3中应该加上list()
        return list(hash_map.values())

    def groupAnagrams_2(self, strs):
        # 计数+哈希
        # 时间复杂度：O(N*K)
        # 空间复杂度：O(N)
        import collections
        if not strs or len(strs) == 0:
            return []
        hash_map = collections.defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            hash_map[tuple(count)].append(s)
        return list(hash_map.values())
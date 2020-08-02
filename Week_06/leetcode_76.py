class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        need = collections.Counter(t)
        window = collections.Counter()
        left, right = 0, 0
        valid = 0
        start, _len = 0, float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                cur = right - left
                if cur < _len:
                    start = left
                    _len = cur
                d = s[left]
                left += 1
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
        return s[start:start + _len] if _len != float('inf') else ''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hash_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        return self.backtrack(hash_map, digits, '', [])

    def backtrack(self, hash_map, digits, track, res):
        if len(digits) == 0:
            res.append(track)
            return res
        for c in hash_map[digits[0]]:
            self.backtrack(hash_map, digits[1:], track + c, res)
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hash_map = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        res = ['']
        for d in digits:
            res = [p + q for p in res for q in hash_map[d]]
        return res
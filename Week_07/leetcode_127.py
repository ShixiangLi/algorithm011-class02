class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        s1, s2 = set(), set()
        s1.add(beginWord)
        s2.add(endWord)
        res = 2
        while s1 and s2:
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for word in s1:
                next_words = [word[:i] + c + word[i + 1:] for i in range(len(word)) for c in 'abcdefghijklmnopqrstuvwxyz']
                for new in next_words:
                    if new in s2:
                        return res
                    if new in wordList:
                        wordList.remove(new)
                        s.add(new)
            s1 = s
            res += 1
        return 0

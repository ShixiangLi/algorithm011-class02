class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        s1, s2 = set(), set()
        s1.add(beginWord)
        s2.add(endWord)
        step = 1
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for word in s1:
                next_words = [word[:i] + c + word[i + 1:] for i in range(len(word)) for c in 'abcdefghijklmnopqrstuvwxyz']
                for mutation in next_words:
                    if mutation in s2: return step
                    if mutation in wordList:
                        wordList.remove(mutation)
                        s.add(mutation)
            s1 = s
        return 0
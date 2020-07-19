class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList: return []
        wordList = set(wordList)
        res = []
        forward, backward = {beginWord:[[beginWord]]}, {endWord:[[endWord]]}
        _len = 2
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
            layer = collections.defaultdict(list)
            while forward:
                word, paths = forward.popitem()
                next_words = [word[:i] + c + word[i + 1:] for i in range(len(word)) for c in 'abcdefghijklmnopqrstuvwxyz']
                for new in next_words:
                    if new in backward:
                        if paths[0][0] == beginWord:
                            res.extend([front + rear[::-1] for front in paths for rear in backward[new]])
                        else:
                            res.extend([front + rear[::-1] for front in backward[new] for rear in paths])
                    if new in wordList:
                        layer[new] += [path + [new] for path in paths]
            _len += 1
            if res and len(res[0]) < _len: break
            wordList -= set(layer.keys())
            forward = layer
        return res
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        bank = set(bank)
        self.res = float('inf')

        def dfs(start, end, step):
            if start == end:
                self.res = min(self.res, step)
                return
            next_words = [start[:i] + c + start[i + 1:] for i in range(len(start)) for c in 'ACGT']
            for new in next_words:
                if new in bank:
                    bank.remove(new)
                    dfs(new, end, step + 1)
                    bank.add(new)

        dfs(start, end, 0)
        return self.res if self.res != float('inf') else -1


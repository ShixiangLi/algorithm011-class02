class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        queue = collections.deque()
        bank = set(bank)
        queue.append((start, 0))
        while queue:
            cur, step = queue.popleft()
            next_words = [cur[:i] + c + cur[i + 1:] for i in range(len(cur)) for c in 'ACGT']
            for mutation in next_words:
                if mutation == end:
                    return step + 1
                if mutation in bank:
                    bank.remove(mutation)
                    queue.append((mutation, step + 1))
        return -1
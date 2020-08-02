class Solution:
    def leastInterval(self, tasks: List[str], need: int) -> int:
        if not tasks: return 0
        n, count = len(tasks), 1
        counter = Counter(tasks).most_common()
        fre = counter[0][1]
        for i in range(1, len(counter)):
            if counter[i][1] == fre:
                count += 1
        res = (fre - 1) * (need + 1) + count
        return res if res >= n else n
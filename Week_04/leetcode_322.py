class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        self.res = float('inf')
        coins.sort(reverse = True)
        self.eager(coins, amount, 0)
        return self.res if self.res != float('inf') else -1
    def eager(self, coins, amount, count):
        if amount == 0:
            self.res = min(self.res, count)
            return
        if coins == []:
            return
        for i in range(amount // coins[0], -1, -1):
            if count + i > self.res: break
            self.eager(coins[1:], amount - i * coins[0], count + i)
class Myheap:
    def __init__(self, capacity):
        self.data_list = []
        self.n = capacity
        self.count = 0
    def insert(self, num):
        if self.count == self.n:
            return False
        self.count += 1
        self.data_list.append(num)
        # 自底向上堆化
        i = self.count - 1
        while i > 0 and num > self.data_list[(i - 1) // 2]:
            self.data_list[i] = self.data_list[(i - 1) // 2]
            i = (i - 1) // 2
        self.data_list[i] = num
    def removeTop(self):
        if self.count == 0:
            return False
        maxValue = self.data_list[0]
        self.count -= 1
        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        self.data_list.pop()
        i = 0
        temp = self.data_list[0]
        while 2 * i + 2 < self.count:
            value = max(self.data_list[2 * i + 1], self.data_list[2 * i + 2])
            if temp >= value:
                break
            elif self.data_list[2 * i + 1] > self.data_list[2 * i + 2]:
                self.data_list[i] = self.data_list[2 * i + 1]
                i = 2 * i + 1
            else:
                self.data_list[i] = self.data_list[2 * i + 2]
                i = 2 * i + 2
        self.data_list[i] = temp
        return maxValue
class MedianFinder:
    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)

    def findMedian(self) -> float:
        self.vals = sorted(self.vals)
        mid1 = (len(self.vals) - 1) // 2
        if len(self.vals) % 2 == 0:
           print(float((self.vals[mid1] + self.vals[mid1 + 1])) / 2)
           return float((self.vals[mid1] + self.vals[mid1 + 1])) / 2
        else:
            print(self.vals[mid1])
            return self.vals[mid1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

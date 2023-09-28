class MedianFinder:
    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        length = len(self.vals)
        if length == 0 or self.vals[-1] <= num:
            self.vals.append(num)
            return
        
        if num <= self.vals[0]:
            self.vals.insert(0, num)
            return
        
        if len(self.vals) == 2:
            self.vals.insert(1, num)
            return
        
        l, r = 0, length - 1
        while l <= r:
            mid = (r + l) // 2
            if self.vals[mid] <= num < self.vals[mid + 1]:
                self.vals.insert(mid + 1, num)
                return
            if self.vals[mid] < num: l = mid + 1
            else: r = mid - 1
        
        self.vals.insert(mid + 1, num)
    
    def findMedian(self) -> float:
        mid = (len(self.vals) - 1) // 2
        if len(self.vals) % 2 == 0: return float((self.vals[mid] + self.vals[mid + 1])) / 2
        else: return self.vals[mid]
           


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

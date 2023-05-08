class MedianFinder:

    def __init__(self):
        self.Min_heap = []
        self.Max_heap = []

    def addNum(self, num: int) -> None:
        if not self.Max_heap or num < -self.Max_heap[0]:
            heapq.heappush(self.Max_heap,-num)
        else:
            heapq.heappush(self.Min_heap,num)

        if len(self.Max_heap) > len(self.Min_heap) + 1:
            heapq.heappush(self.Min_heap,-heapq.heappop(self.Max_heap))
        elif len(self.Min_heap) > len(self.Max_heap):
            heapq.heappush(self.Max_heap,-heapq.heappop(self.Min_heap))
    def findMedian(self) -> float:
        if len(self.Min_heap) == len(self.Max_heap):
            return (self.Min_heap[0] + -self.Max_heap[0])/2
        else:
            return -self.Max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
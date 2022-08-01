# Find Median from Data Stream
# keep two heaps (min heap + max heap),
# len of max heap always larger than min heap, max heap will have median

class MedianFinder:
    # space: O(n)
    def __init__(self):
        self.small = [] # max heap (inverse min)
        self.large = [] # min heap, len must >= self.small
        
    # time: O(logN)
    def addNum(self, num: int) -> None:
        # add num to large, move top to small
        heappush(self.large, num)
        heappush(self.small, -heappop(self.large))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    # time: O(1)
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0]-self.small[0])/2.0
        else:
            return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

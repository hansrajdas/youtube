"""
https://leetcode.com/problems/find-median-from-data-stream/

Complexity
----------
Time:
  addNum: O(logn)
  findMedian: O(1)
Space: O(n)
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

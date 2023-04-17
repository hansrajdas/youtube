"""
https://leetcode.com/problems/find-median-from-data-stream/

Complexity
----------
Time:
  addNum: O(n)
  findMedian: O(1)
Space: O(n)

NOTE: This solution is NOT accepted, gives TLE error.
"""

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        i = len(self.nums) - 1
        while i >= 1 and self.nums[i - 1] > self.nums[i]:
            self.nums[i - 1], self.nums[i] = self.nums[i], self.nums[i - 1]
            i -= 1

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2:
            return self.nums[mid]
        return (self.nums[mid - 1] + self.nums[mid]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

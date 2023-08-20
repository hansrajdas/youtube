"""
https://leetcode.com/problems/binary-search/description/

Complexity
----------
Time: O(logn)
Space: O(logn)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(low, high):
            if high < low:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid + 1, high)
            return binarySearch(low, mid - 1)
        return binarySearch(0, len(nums) - 1)

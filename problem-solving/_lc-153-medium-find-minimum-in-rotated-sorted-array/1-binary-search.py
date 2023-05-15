"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Complexity
----------
Time: O(logn)
Space: O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]

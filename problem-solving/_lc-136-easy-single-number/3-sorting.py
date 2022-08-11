"""
https://leetcode.com/problems/single-number/

Complexity
----------
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i - 1] != nums[i]:
                return nums[i - 1]
        return nums[len(nums) - 1]

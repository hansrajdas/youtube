"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res

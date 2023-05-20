"""
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n^2)

NOTE: This solution is not accepted, gives "Memory limit exceeded"
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def _lengthOfLIS(prev, idx):
            if idx == len(nums):
                return 0
            if (prev, idx) in cache:
                return cache[(prev, idx)]
            taken = 0
            notTaken = _lengthOfLIS(prev, idx + 1)
            if prev < nums[idx]:
                taken = 1 + _lengthOfLIS(nums[idx], idx + 1)
            cache[(prev, idx)] = max(taken, notTaken)
            return cache[(prev, idx)]

        return _lengthOfLIS(-math.inf, 0)

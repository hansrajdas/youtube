"""
https://leetcode.com/problems/house-robber/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def robMax(idx):
            if idx >= len(nums):
                return 0
            if idx in cache:
                return cache[idx]
            notTaken = robMax(idx + 1)  # Skip current but rob next
            taken = nums[idx] + robMax(idx + 2)  # Rob current and skip next
            cache[idx] = max(taken, notTaken)
            return cache[idx]
        return robMax(0)

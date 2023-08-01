"""
https://leetcode.com/problems/target-sum/

Complexity
----------
Time: O(n*S)
Space: O(n*S)
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def targetSum(s,  idx):
            if idx == len(nums):
                if s == target:
                    return 1
                return 0
            if (s, idx) in cache:
                return cache[(s, idx)]
            cache[(s, idx)] = targetSum(s + nums[idx], idx + 1) + targetSum(s - nums[idx], idx + 1)
            return cache[(s, idx)]

        cache = {}
        return targetSum(0, 0)

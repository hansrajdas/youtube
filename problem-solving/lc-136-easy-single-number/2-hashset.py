"""
https://leetcode.com/problems/single-number/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

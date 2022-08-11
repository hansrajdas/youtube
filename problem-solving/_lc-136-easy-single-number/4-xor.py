"""
https://leetcode.com/problems/single-number/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return x

"""
https://leetcode.com/problems/climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        away = 1
        away2 = 2
        res = n
        for v in range(3, n + 1):
            res = away + away2
            away = away2
            away2 = res
        return res

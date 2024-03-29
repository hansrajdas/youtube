"""
https://leetcode.com/problems/climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(N)
"""

from functools import lru_cache

class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

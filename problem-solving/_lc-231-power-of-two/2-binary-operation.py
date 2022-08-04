"""
https://leetcode.com/problems/power-of-two/

Complexity
----------
Time: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0

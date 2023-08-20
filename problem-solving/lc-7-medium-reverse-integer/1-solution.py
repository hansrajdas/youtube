"""
https://leetcode.com/problems/reverse-integer/

Complexity
----------
Time: O(logn)
Space: O(1)

NOTE: log base 10
"""

MAX = (1 << 31)
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        res = 0
        while x:
            res = (res * 10) + (x % 10)
            x //= 10
        res = sign * res
        if res < -MAX or res > MAX - 1:
            return 0
        return res

"""
https://leetcode.com/problems/add-digits/

Complexity
----------
Time: O(logn)  // base 10
Space: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        res = 0
        while num:
            res += num % 10
            num //= 10
        return self.addDigits(res)

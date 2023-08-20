"""
https://leetcode.com/problems/palindrome-number/

Complexity
----------
Time: O(logn)  // Base 10
Space: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev, n = 0, x
        while n > 0:
            d = n % 10
            n //= 10
            rev = (rev << 3) + (rev << 1) + d
        return rev == x

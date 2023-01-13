"""
https://leetcode.com/problems/count-the-digits-that-divide-a-number/

Complexity
----------
Time: O(logn)
Space: O(logn)

NOTE: Base of log is 10 here.
"""

class Solution:
    def countDigits(self, num: int) -> int:
        digits = []
        n = num
        while n:
            digits.append(n % 10)
            n //= 10
        count = 0
        for x in digits:
            if num % x == 0:
                count += 1
        return count

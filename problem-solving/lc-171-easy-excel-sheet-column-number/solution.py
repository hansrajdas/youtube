"""
https://leetcode.com/problems/excel-sheet-column-number/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        power = 1
        for c in columnTitle[::-1]:
            res += (ord(c) - 64) * power
            power *= 26
        return res

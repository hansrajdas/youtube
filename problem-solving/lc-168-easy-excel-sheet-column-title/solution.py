"""
https://leetcode.com/problems/excel-sheet-column-title/

Complexity
----------
Time and space complexity: O(logn), base = 26
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            v = columnNumber % 26
            ch = chr(65 + v)
            res.append(ch)
            columnNumber //= 26
        res.reverse()
        return ''.join(res)

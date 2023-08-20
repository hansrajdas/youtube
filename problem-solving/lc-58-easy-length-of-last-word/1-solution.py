"""
https://leetcode.com/problems/length-of-last-word/

Complexity
----------
Time: O(n)
Space: O(1)

n = length of whole string
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        n = len(s) - 1
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            n -= 1
            l += 1
        return l

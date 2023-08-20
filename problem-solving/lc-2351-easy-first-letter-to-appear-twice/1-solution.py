"""
https://leetcode.com/problems/first-letter-to-appear-twice/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        S = set()
        for c in s:
            if c in S:
                return c
            S.add(c)

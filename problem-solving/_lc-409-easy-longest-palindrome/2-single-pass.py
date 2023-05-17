"""
https://leetcode.com/problems/longest-palindrome/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for c in s:
            if c in seen:
                seen.remove(c)
            else:
                seen.add(c)
        if len(seen) > 0:
            return len(s) - len(seen) + 1
        return len(s)

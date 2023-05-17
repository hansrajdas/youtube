"""
https://leetcode.com/problems/longest-palindromic-substring/

Complexity
----------
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        for i in range(n):
            # Odd len palindrome - having center char
            l = i - 1
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if end - start < r - l:
                    start, end = l, r
                l -= 1
                r += 1
            # Even len palindrome - don't have center char
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if end - start < r - l:
                    start, end = l, r
                l -= 1
                r += 1
        return s[start:end + 1]

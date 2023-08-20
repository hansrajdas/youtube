"""
https://leetcode.com/problems/longest-palindromic-substring/

Complexity
----------
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s, l, r, start, end):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if end - start < r - l:
                start, end = l, r
            l -= 1
            r += 1
        return start, end

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        for i in range(n):
            # Odd len palindrome - having center char at i
            start, end = self.isPalindrome(s, i - 1, i + 1, start, end)

            # Even len palindrome - don't have center char
            start, end = self.isPalindrome(s, i, i + 1, start, end)
        return s[start:end + 1]

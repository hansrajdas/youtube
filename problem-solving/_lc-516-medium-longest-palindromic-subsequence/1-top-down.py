"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n^2)
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        def lps(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) in cache:
                return cache[(l, r)]
            if s[l] == s[r]:
                cache[(l, r)] = 2 + lps(l + 1, r - 1)
            else:
                cache[(l, r)] = max(lps(l + 1, r), lps(l, r - 1))
            return cache[(l, r)]
        return lps(0, len(s) - 1)

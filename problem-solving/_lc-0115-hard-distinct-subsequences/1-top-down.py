"""
https://leetcode.com/problems/distinct-subsequences/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def _numDistinct(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == t[j]:
                cache[(i, j)] = _numDistinct(i + 1, j) + _numDistinct(i + 1, j + 1)
            else:
                cache[(i, j)] = _numDistinct(i + 1, j)
            return cache[(i, j)]
        return _numDistinct(0, 0)

"""
https://leetcode.com/problems/unique-paths/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def getUniquePaths(r, c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 or c == n - 1:
                return 1
            if (r, c ) not in cache:
                cache[(r, c)] = getUniquePaths(r + 1, c) + getUniquePaths(r, c + 1)
            return cache[(r, c)]
        cache = {}
        return getUniquePaths(0, 0)

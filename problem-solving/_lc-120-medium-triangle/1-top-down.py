"""
https://leetcode.com/problems/triangle/

Complexity
----------
Time: O(n*n)
Space: O(n*n)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cache = {}
        def solve(r, c):
            if r >= n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = triangle[r][c] + min(solve(r + 1, c),
                                                 solve(r + 1, c + 1))
            return cache[(r, c)]
        return solve(0, 0)

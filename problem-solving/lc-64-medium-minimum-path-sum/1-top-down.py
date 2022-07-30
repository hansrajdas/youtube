"""
https://leetcode.com/problems/minimum-path-sum/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cache = {}
        def minPath(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in cache:
                return cache[(r, c)]
            if r == rows - 1:
                cache[(r, c)] = grid[r][c] + minPath(r, c + 1)
            elif c == cols - 1:
                cache[(r, c)] = grid[r][c] + minPath(r + 1, c)
            else:
                cache[(r, c)] = grid[r][c] + min(minPath(r, c + 1),
                                                 minPath(r + 1, c))
            return cache[(r, c)]
        return minPath(0, 0)

"""
https://leetcode.com/problems/unique-paths-ii

Complexity
----------
Time: O(rows*cols)
Space: O(rows*cols)
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = {}
        def paths(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or obstacleGrid[r][c]:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = paths(r + 1, c) + paths(r, c + 1)
            return cache[(r, c)]
        return paths(0, 0)

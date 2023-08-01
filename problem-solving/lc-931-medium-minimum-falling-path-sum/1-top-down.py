"""
https://leetcode.com/problems/minimum-falling-path-sum/

Complexity
----------
Time and space: O(n*n)
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        n = len(matrix)
        def minPath(r, c):
            if r == n - 1:
                return matrix[r][c]
            if (r, c) in cache:
                return cache[(r, c)]
            if c == 0:
                cache[(r, c)] = matrix[r][c] + min(
                    minPath(r + 1, c),
                    minPath(r + 1, c + 1))
            elif c == n - 1:
                cache[(r, c)] = matrix[r][c] + min(
                    minPath(r + 1, c - 1),
                    minPath(r + 1, c))
            else:
                cache[(r, c)] = matrix[r][c] + min(
                    minPath(r + 1, c - 1),
                    minPath(r + 1, c),
                    minPath(r + 1, c + 1))
            return cache[(r, c)]
        res = math.inf
        for c in range(n):
            res = min(res, minPath(0, c))
        return res

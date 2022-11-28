"""
https://leetcode.com/problems/knight-probability-in-chessboard/

Complexity
----------
Time: O(k*n*n)
Space: O(k*n*n)
"""

delta = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def knightProbab(k, r, c):
            if 0 > r or r >= n or 0 > c or c >= n:
                return 0
            if k == 0:
                return 1
            if (k, r, c) in cache:
                return cache[(k, r, c)]
            res = 0
            for dr, dc in delta:
                res += knightProbab(k - 1, r + dr, c + dc) / 8
            cache[(k, r, c)] = res
            return cache[(k, r, c)]
        cache = {}
        return knightProbab(k, row, column)

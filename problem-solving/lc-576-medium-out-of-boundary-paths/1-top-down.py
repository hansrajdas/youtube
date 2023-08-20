"""
https://leetcode.com/problems/out-of-boundary-paths

Complexity
----------
Time: O(mnN)
Space: O(mnN)

N = maxMove
"""

M = 1000000007
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        def paths(r, c, movesLeft):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if movesLeft == 0:
                return 0
            if (r, c, movesLeft) in cache:
                return cache[(r, c, movesLeft)]
            cache[(r, c, movesLeft)] = (
                paths(r, c - 1, movesLeft - 1) +
                paths(r, c + 1, movesLeft - 1) +
                paths(r - 1, c, movesLeft - 1) +
                paths(r + 1, c, movesLeft - 1)
            ) % M
            return cache[(r, c, movesLeft)]
        return paths(startRow, startColumn, maxMove)

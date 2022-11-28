"""
https://leetcode.com/problems/knight-probability-in-chessboard/

Complexity
----------
Time: O(k*n*n)
Space: O(k*n*n)

NOTE
----
This can also be solved with O(n*n) time complexity as we are only accessing dp[k-1] for solving dp[k]
"""

delta = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1
        for idx in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in delta:
                        oldRow = r - dr
                        oldCol = c - dc
                        if 0 <= oldRow < n and 0 <= oldCol < n:
                            dp[idx][r][c] += dp[idx - 1][oldRow][oldCol] / 8

        res = 0
        for r in range(n):
            for c in range(n):
                res += dp[k][r][c]
        return res

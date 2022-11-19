"""
https://leetcode.com/problems/unique-paths/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n + 1) for _ in range(m + 1)]
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]

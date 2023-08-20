"""
https://leetcode.com/problems/unique-paths/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if r == 1 or c == 1:
                    dp[r][c] = 1
                    continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]

"""
https://leetcode.com/problems/triangle/

Complexity
----------
Time: O(n*n)
Space: O(n*n)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle[r]) for r in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    dp[r][c] = triangle[r][c] + dp[r - 1][c]
                elif c == len(triangle[r]) - 1:
                    dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]
                else:
                    dp[r][c] = triangle[r][c] + min(dp[r - 1][c], dp[r - 1][c - 1])
        return min(dp[-1])

"""
https://leetcode.com/problems/maximal-square/

Complexity
----------
Time: O(mn)
Space: O(n)  // Number of cols
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        maxlen = prev = 0
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                temp = dp[c]
                if matrix[r - 1][c - 1] == '1':
                    dp[c] = min(dp[c - 1], dp[c], prev) + 1
                    maxlen = max(maxlen, dp[c])
                else:
                    dp[c] = 0
                prev = temp
        return maxlen * maxlen

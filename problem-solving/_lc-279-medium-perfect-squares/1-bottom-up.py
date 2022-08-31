"""
https://leetcode.com/problems/perfect-squares/

Complexity
----------
Time: O(n*sqrt(n))
Space: O(n)
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            sq = 1
            while sq * sq <= i:
                dp[i] = min(dp[i], dp[i - sq * sq] + 1)
                sq += 1
        return dp[n]

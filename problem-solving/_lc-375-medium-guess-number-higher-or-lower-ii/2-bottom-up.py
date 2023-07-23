"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

Complexity
----------
Time: O(n^3)
Space: O(n^2)
"""

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # This loop in run in reverse order because in the recurrence relation,
        # we are accessing future index (g + 1) of l.
        for l in range(n - 1, 0, -1):
            for h in range(l + 1, n + 1):
                dp[l][h] = math.inf
                for g in range(l, h):
                    temp = g + max(dp[l][g - 1], dp[g + 1][h])
                    dp[l][h] = min(dp[l][h], temp)
        return dp[1][n]

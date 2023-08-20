"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

Complexity
----------
Time: O(n*k*target)
Space: O(n*target)
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for tg in range(1, target + 1):
                for x in range(1, min(k, tg) + 1):
                    dp[i][tg] = dp[i][tg] + dp[i - 1][tg - x]
        return dp[n][target] % (10**9 + 7)

"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        for idx in range(2, n + 1):
            dp[idx] = min(dp[idx - 1] + cost[idx - 1],
                          dp[idx - 2] + cost[idx - 2])
        return dp[n]

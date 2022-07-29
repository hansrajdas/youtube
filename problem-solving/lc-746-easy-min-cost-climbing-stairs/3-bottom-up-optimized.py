"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(1)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        away1 = away2 = 0
        for idx in range(2, n + 1):
            res = min(cost[idx - 1] + away1,
                      cost[idx - 2] + away2)
            away2 = away1
            away1 = res
        return res

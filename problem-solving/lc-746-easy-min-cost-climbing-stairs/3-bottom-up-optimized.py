"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(1)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_away = two_away = 0
        n = len(cost)
        for i in range(2, n + 1):
            res = min(
                cost[i - 1] + one_away,
                cost[i - 2] + two_away
            )
            two_away = one_away
            one_away = res
        return res

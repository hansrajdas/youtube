"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Complexity
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(idx):
            if idx >= len(cost):
                return 0
            if idx in cache:
                return cache[idx]
            cache[idx] = cost[idx] + min(minCost(idx + 1),
                                         minCost(idx + 2))
            return cache[idx]

        cache = {}
        return min(minCost(0), minCost(1))

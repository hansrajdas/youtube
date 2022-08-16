"""
https://leetcode.com/problems/minimum-cost-for-tickets/

Time and space: O(LAST_DAY)
"""

# Bottom up approach
# Time and space: O(LAST_DAY)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)
        daysSet = set(days)
        for d in range(1, lastDay + 1):
            if d not in daysSet:
                dp[d] = dp[d - 1]
            else:
                dp[d] = min(costs[0] + dp[d - 1],
                            costs[1] + dp[max(0, d - 7)],
                            costs[2] + dp[max(0, d - 30)])
        return dp[-1]

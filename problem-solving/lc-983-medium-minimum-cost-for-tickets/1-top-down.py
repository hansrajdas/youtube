"""
https://leetcode.com/problems/minimum-cost-for-tickets/

Time and space: O(LAST_DAY)
"""

# Top down
# Time and space: O(LAST_DAY)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daysSet = set(days)
        cache = {}
        def minCost(day):
            if day <= 0:
                return 0
            if day in cache:
                return cache[day]
            if day not in daysSet:
                return minCost(day - 1)
            dayPass = costs[0] + minCost(day - 1)
            weekPass = costs[1] + minCost(day - 7)
            monthPass = costs[2] + minCost(day - 30)
            cache[day] = min(dayPass, weekPass, monthPass)
            return cache[day]
        return minCost(days[-1])

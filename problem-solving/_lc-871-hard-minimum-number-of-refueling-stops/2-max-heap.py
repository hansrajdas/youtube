"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/

Complexity
----------
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target, math.inf))
        ans = 0
        pq = []  # Max heap, add negative values
        prev = 0
        tank = startFuel
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:
                ans += 1
                tank += -heapq.heappop(pq)
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return ans

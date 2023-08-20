"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/

Complexity
----------
Time: O(n*n)
Space: O(n)
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i in range(len(stations)):
            location = stations[i][0]
            capacity = stations[i][1]
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t+ 1], dp[t] + capacity)

        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1

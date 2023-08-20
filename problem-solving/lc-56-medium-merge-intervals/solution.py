"""
https://leetcode.com/problems/merge-intervals/

Complexity
----------
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1
        return res

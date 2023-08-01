"""
https://leetcode.com/problems/triangle/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        res = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]

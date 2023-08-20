"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Complexity
----------
Time: O(N^3)
Space: O(N^2)

Reference: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/294265/python-in-depth-explanation-dp-for-beginners/
"""

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        cache = {}
        def dfs(left, right):
            # Need atleast 3 points to make triangle.
            if right - left < 2:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            cache[(left, right)] = math.inf
            for mid in range(left + 1, right):
                cache[(left, right)] = min(cache[(left, right)], values[left]*values[mid]*values[right] + dfs(left, mid) + dfs(mid, right))
            return cache[(left, right)]
        return dfs(0, len(values) - 1)

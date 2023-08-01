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
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for l in range(2, n):
            for left in range(n - l):
                right = left + l
                dp[left][right] = math.inf
                for mid in range(left + 1, right):
                    dp[left][right] = min(
                        dp[left][right],
                        values[left]*values[mid]*values[right] + dp[left][mid] + dp[mid][right])

        return dp[0][n - 1]

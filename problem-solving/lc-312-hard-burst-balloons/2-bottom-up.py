"""
https://leetcode.com/problems/burst-balloons/

Complexity
----------
Time: O(n^3)
Space: O(n^2)

Reference
---------
Explanation: https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
Code: https://leetcode.com/problems/burst-balloons/solutions/76228/share-some-analysis-and-explanations/
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = [1] + nums + [1]
        n = len(N)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for l in range(n - k):
                r = l + k
                for m in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        N[l]*N[m]*N[r] + dp[l][m] + dp[m][r])
        return dp[0][n - 1]

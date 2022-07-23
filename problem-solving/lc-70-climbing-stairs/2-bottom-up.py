# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for v in range(3, n + 1):
            dp[v] = dp[v - 1] + dp[v - 2]
        return dp[n]

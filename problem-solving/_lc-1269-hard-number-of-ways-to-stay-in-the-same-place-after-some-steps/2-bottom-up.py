"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*min(S, N))
Space: O(S*min(S, N))

S = Steps
N = arrLen
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 1000000007
        maxPos = min(steps, arrLen)
        dp = [[0] * maxPos for _ in range(steps + 1)]
        dp[0][0] = 1
        for s in range(1, steps + 1):
            for idx in range(maxPos):
                dp[s][idx] = dp[s - 1][idx] % M
                if idx > 0:
                    dp[s][idx] = (dp[s][idx] + dp[s - 1][idx - 1]) % M
                if idx < maxPos - 1:
                    dp[s][idx] = (dp[s][idx] + dp[s - 1][idx + 1]) % M
        return dp[steps][0]

"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*min(S, N))
Space: O(min(S, N))

S = Steps
N = arrLen
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 1000000007
        maxPos = min(steps, arrLen)
        dp = [0] * maxPos
        dp[0] = 1
        for _ in range(1, steps + 1):  # Or range(steps)
            temp = [0] * maxPos
            for idx in range(maxPos):
                temp[idx] = dp[idx]
                if idx > 0:
                    temp[idx] = (temp[idx] + dp[idx - 1]) % M
                if idx < maxPos - 1:
                    temp[idx] = (temp[idx] + dp[idx + 1]) % M
            dp = temp
        return dp[0]

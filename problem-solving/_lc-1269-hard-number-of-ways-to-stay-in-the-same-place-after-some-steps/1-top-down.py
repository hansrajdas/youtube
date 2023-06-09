"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*N)
Space: O(S*N)

S = Steps
N = arrLen
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 1000000007
        cache = {}
        def ways(idx, stepsLeft):
            if idx < 0 or idx == arrLen:
                return 0
            if stepsLeft == 0:
                if idx == 0:
                    return 1
                return 0
            if (idx, stepsLeft) in cache:
                return cache[(idx, stepsLeft)]
            cache[(idx, stepsLeft)] = (
                ways(idx, stepsLeft - 1) +
                ways(idx - 1, stepsLeft - 1) +
                ways(idx + 1, stepsLeft - 1)
            ) % M
            return cache[(idx, stepsLeft)]
        return ways(0, steps)


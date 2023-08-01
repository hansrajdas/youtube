"""
https://leetcode.com/problems/knight-dialer/

Complexity
----------
Time: O(n)
Space: O(n)

Complexity has some constant factors also multiplied `3 * 4 * 8`
"""

pos = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[[0 for _ in range(n + 1)] for _ in range(3)] for _ in range(4)]

        for r in range(4):
            for c in range(3):
                if (r, c) not in [(3, 0), (3, 2)]:
                    dp[r][c][1] = 1

        for l in range(2, n + 1):
            for r in range(4):
                for c in range(3):
                    if (r, c) in [(3, 0), (3, 2)]:
                        continue
                    for r0, c0 in pos:
                        nr = r - r0
                        nc = c - c0
                        if nr >= 0 and nr < 4 and nc >= 0 and nc < 3:
                            dp[r][c][l] += dp[nr][nc][l - 1]
        res = 0
        for r in range(4):
            for c in range(3):
                res += dp[r][c][n]
        return res % 1000000007

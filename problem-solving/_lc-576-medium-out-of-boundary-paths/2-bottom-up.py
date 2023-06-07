"""
https://leetcode.com/problems/out-of-boundary-paths

Complexity
----------
Time: O(mnN)
Space: O(mn)

N = maxMove

Reference: https://leetcode.com/problems/out-of-boundary-paths/editorial/ [Approach 3]
"""

M = 1000000007
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        for _ in range(maxMove):
            # if we alter the dp array, now some of the entries will correspond to x−1 moves and the updated ones will correspond to x moves so taking temp.
            temp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    # If on boundary then in next move we can go out of boundary so sum all numbers to reach boundary till previous move.
                    if r == 0: count = (count + dp[r][c]) % M
                    if r == m - 1: count = (count + dp[r][c]) % M
                    if c == 0: count = (count + dp[r][c]) % M
                    if c == n - 1: count = (count + dp[r][c]) % M

                    # Update temp and retain dp.
                    if r > 0: temp[r][c] = dp[r - 1][c]
                    if r < m - 1: temp[r][c] = (temp[r][c] + dp[r + 1][c]) % M
                    if c > 0: temp[r][c] = (temp[r][c] + dp[r][c - 1]) % M
                    if c < n - 1: temp[r][c] = (temp[r][c] + dp[r][c + 1]) % M
            dp = temp
        return count

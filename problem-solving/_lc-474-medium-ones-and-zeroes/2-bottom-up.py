"""
https://leetcode.com/problems/ones-and-zeroes/

Complexity
----------
Time: O(L*m*n)  // L = number of strings
Space: O(m*n)
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones = 0
            for c in s:
                if c == '1':
                    ones += 1
            zeros = len(s) - ones
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)
        return dp[m][n]

"""
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(n)
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        dp = [[0] * 5 for _ in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        for idx in range(1, n):
            # Previous counts
            a, e, i, o, u = dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][2], dp[idx - 1][3], dp[idx - 1][4]

            # a can be after e, i or u, and so on...
            dp[idx][0] = (e + i + u) % M
            dp[idx][1] = (a + i) % M
            dp[idx][2] = (e + o) % M
            dp[idx][3] = i % M
            dp[idx][4] = (i + o) % M
        return sum(dp[n - 1]) % M

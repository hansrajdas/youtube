"""
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(5*n) => O(n)
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        dp = [[0] * 5 for _ in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        for idx in range(1, n):
            # Previous counts
            a, e, i, o, u = dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][2], dp[idx - 1][3], dp[idx - 1][4]
            for c in ('a', 'e', 'i', 'o', 'u'):
                # After which chars, we can have current char
                if c == 'a':
                    dp[idx][0] = (e + i + u) % M
                elif c == 'e':
                    dp[idx][1] = (a + i) % M
                elif c == 'i':
                    dp[idx][2] = (e + o) % M
                elif c == 'o':
                    dp[idx][3] = i % M
                else:
                    dp[idx][4] = (i + o) % M
        return sum(dp[n - 1]) % M

"""
https://leetcode.com/problems/unique-paths/

Complexity
----------
Time: O(m*n)
Space: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [0] * (n + 1)
        prev = curr[:]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if r == 1 or c == 1:
                    curr[c] = 1
                    continue
                curr[c] = prev[c] + curr[c - 1]
            prev = curr[:]
        return curr[n]

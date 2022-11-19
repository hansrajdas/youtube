"""
https://leetcode.com/problems/unique-paths/

Complexity
----------
Time: O(m*n)
Space: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [1] * (n + 1)
        prev = curr[:]
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                curr[c] = prev[c] + curr[c - 1]
            prev = curr[:]
        return curr[n]

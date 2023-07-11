"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cache = {}
        m, n = len(s1), len(s2)
        def minDel(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            if i == len(s1):
                return sum(ord(s2[x]) for x in range(j, n))
            if j == len(s2):
                return sum(ord(s1[x]) for x in range(i, m))
            if (i, j) in cache:
                return cache[(i, j)]
            if s1[i] == s2[j]:
                cache[(i, j)] = minDel(i + 1, j + 1)
            else:
                cache[(i, j)] = min(
                    ord(s1[i]) + minDel(i + 1, j),
                    ord(s2[j]) + minDel(i, j + 1))
            return cache[(i, j)]
        return minDel(0, 0)

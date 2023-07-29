"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Complexity
----------
Time: O(m*n)
Space: O(m*n)

NOTE
----
This can be solved in linear time using standard pattern matching algorithms like
KMP, Rabin karp, ...
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
                if j == n - 1:
                    return i
        return -1

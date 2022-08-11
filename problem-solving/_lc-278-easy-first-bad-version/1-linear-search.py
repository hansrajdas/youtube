"""
https://leetcode.com/problems/first-bad-version/

Complexity
----------
Time: O(n)
Space: O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for v in range(1, n + 1):
            if isBadVersion(v):
                return v

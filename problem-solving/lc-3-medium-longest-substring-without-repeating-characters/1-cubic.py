"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n^3)
Space: O(n)

NOTE: This solution is not accepted, gives TLE
"""

def allUniq(start, end, s):
    seen = set()
    for i in range(start, end + 1):
        if s[i] in seen:
            return False
        seen.add(s[i])
    return True

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mx = 0
        for i in range(n):
            for j in range(i, n):
                if allUniq(i, j, s):
                    mx = max(mx, j - i + 1)
        return mx

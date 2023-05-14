"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n^2)
Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mx = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(s[j])
                if len(seen) < j - i + 1:
                    break
                mx = max(mx, len(seen))
        return mx

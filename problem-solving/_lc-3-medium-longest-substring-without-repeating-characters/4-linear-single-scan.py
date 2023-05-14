"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n)
Space: O(n)

Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/1729/11-line-simple-java-solution-o-n-with-explanation/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = collections.Counter()
        left = right = 0
        mx = 0
        while right < len(s):
            if s[right] in mp:
                # For input "pwwkew" we has to make left = 2 (not 1) from 0
                left = max(left, mp[s[right]] + 1)
            mx = max(mx, right - left + 1)
            mp[s[right]] = right
            right += 1
        return mx

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        mp = collections.Counter()
        left = right = 0
        while right < len(s):  # Can also be done using for loop
            mp[s[right]] += 1
            while mp[s[right]] > 1:
                mp[s[left]] -= 1
                left += 1
            mx = max(mx, right - left + 1)
            right += 1
        return mx

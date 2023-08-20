"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1

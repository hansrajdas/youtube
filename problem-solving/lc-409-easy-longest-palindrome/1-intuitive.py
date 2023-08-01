"""
https://leetcode.com/problems/longest-palindrome/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        oddCount = False
        ans = 0
        for c in count:
            if count[c] % 2 == 0:
                ans += count[c]
            else:
                ans += count[c] - 1
                oddCount = True
        if oddCount:
            ans += 1
        return ans

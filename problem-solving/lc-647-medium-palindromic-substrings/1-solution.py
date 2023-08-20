"""
https://leetcode.com/problems/palindromic-substrings/

Complexity
----------
Time: O(n^2)
Space: O(1)
"""

def countPalindrome(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        count += 1
    return count

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        mid = 0
        while mid < len(s):
            count += countPalindrome(s, mid - 1, mid + 1)
            count += countPalindrome(s, mid, mid + 1)
            mid += 1
        return count

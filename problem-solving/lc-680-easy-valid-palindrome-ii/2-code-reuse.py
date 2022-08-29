"""
https://leetcode.com/problems/valid-palindrome-ii/

Complexity
----------
Time: O(n)
Space: O(1)
"""

def isPalindrome(s, l, r, mismatches=0):
    if mismatches > 1:
        return False
    while l < r:
        if s[l] != s[r]:
            return (isPalindrome(s, l + 1, r, mismatches + 1) or
                    isPalindrome(s, l, r - 1, mismatches + 1))
        l += 1
        r -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return isPalindrome(s, 0, len(s) - 1)

"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        res = 0
        for w in words:
            wr = w[::-1]
            if wr in seen and seen[wr] > 0:
                res += 4
                seen[wr] -= 1
            else:
                seen[w] += 1

        for w in seen:
            if seen[w] > 0 and w[0] == w[1]:
                return res + 2
        return res

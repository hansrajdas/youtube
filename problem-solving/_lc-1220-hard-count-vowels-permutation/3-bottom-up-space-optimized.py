"""
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time: O(5*n) => O(n)
Space: O(1)
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        a = e = i = o = u = 1
        for idx in range(1, n):
            # Previous counts
            pa, pe, pi, po, pu = a, e, i, o, u
            for c in ('a', 'e', 'i', 'o', 'u'):
                # After which chars, we can have current char
                if c == 'a':
                    a = (pe + pi + pu) % M
                elif c == 'e':
                    e = (pa + pi) % M
                elif c == 'i':
                    i = (pe + po) % M
                elif c == 'o':
                    o = pi % M
                else:
                    u = (pi + po) % M
        return (a + e + i + o + u) % M

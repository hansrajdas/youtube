"""
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        a = e = i = o = u = 1
        for idx in range(1, n):
            # Previous counts
            pa, pe, pi, po, pu = a, e, i, o, u

            # a can be after e, i or u, and so on...
            a = (pe + pi + pu) % M
            e = (pa + pi) % M
            i = (pe + po) % M
            o = pi % M
            u = (pi + po) % M
        return (a + e + i + o + u) % M

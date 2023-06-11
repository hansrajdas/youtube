"""
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(5*n) => O(n)
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        cache = collections.defaultdict(int)
        # '*' is used to handle initial condition, when we don't
        # previous char and can have any of 5 vowels.
        nextChars = {
            '*': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a'],
        }
        def getCount(lastChar, vowelCount):
            if vowelCount == n:
                return 1
            if (lastChar, vowelCount) in cache:
                return cache[(lastChar, vowelCount)]
            for v in nextChars[lastChar]:
                cache[(lastChar, vowelCount)] = (
                    cache[(lastChar, vowelCount)] +
                    getCount(v, vowelCount + 1)) % M
            return cache[(lastChar, vowelCount)]
        return getCount('*', 0)

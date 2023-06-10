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
        vowelRule = {
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
            if lastChar is None:
                nextVowels = ['a', 'e', 'i', 'o', 'u']
            else:
                nextVowels = vowelRule[lastChar]
            for v in nextVowels:
                cache[(lastChar, vowelCount)] = (
                    cache[(lastChar, vowelCount)] +
                    getCount(v, vowelCount + 1)) % M
            return cache[(lastChar, vowelCount)]
        return getCount(None, 0)

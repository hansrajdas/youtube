"""
https://leetcode.com/problems/ones-and-zeroes/

Complexity
----------
Time and space: O(L*m*n)  // L = number of strings
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = []
        for s in strs:
            ones = 0
            for c in s:
                if c == '1':
                    ones += 1
            counter.append({'ones': ones, 'zeros': len(s) - ones})
        cache = {}
        def largestSubset(idx, zeros, ones):
            if idx == len(counter) or (zeros == 0 and ones == 0):
                return 0
            if (idx, zeros, ones) in cache:
                return cache[(idx, zeros, ones)]
            if counter[idx]['zeros'] > zeros or counter[idx]['ones'] > ones:
                cache[(idx, zeros, ones)] = largestSubset(idx + 1, zeros, ones)
                return cache[(idx, zeros, ones)]
            cache[(idx, zeros, ones)] = max(
                largestSubset(idx + 1, zeros, ones),
                largestSubset(idx + 1, zeros - counter[idx]['zeros'], ones - counter[idx]['ones']) + 1)
            return cache[(idx, zeros, ones)]
        return largestSubset(0, m, n)

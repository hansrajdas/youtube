"""
https://leetcode.com/problems/unique-binary-search-trees/

Complexity
----------
Time: O(n^2)
Space: O(n)

Reference: https://leetcode.com/problems/unique-binary-search-trees/solutions/1565543/c-python-5-easy-solutions-w-explanation-optimization-from-brute-force-to-dp-to-catalan-o-n/
"""

class Solution:
    def __init__(self):
        self.cache = collections.defaultdict(int)
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        for i in range(1, n + 1):
            self.cache[n] += self.numTrees(i - 1) * self.numTrees(n - i)
        return self.cache[n]

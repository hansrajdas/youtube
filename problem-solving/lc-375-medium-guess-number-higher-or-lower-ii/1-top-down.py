"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

Complexity
----------
Time: O(n^3)
Space: O(n^2)
"""

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = {}
        def dfs(low, high):
            if low >= high:
                return 0
            if (low, high) in cache:
                return cache[(low, high)]
            cache[(low, high)] = math.inf
            for guess in range(low, high + 1):
                temp = guess + max(dfs(low, guess - 1), dfs(guess + 1, high))
                cache[(low, high)] = min(cache[(low, high)], temp)
            return cache[(low, high)]
        return dfs(1, n)

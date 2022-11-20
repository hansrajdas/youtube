"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

Complexity
----------
Time: O(n*k*target)
Space: O(n*target)
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def rollsToTarget(dice, tg):
            if dice == 0:
                if tg == 0:
                    return 1
                return 0
            if (dice, tg) in cache:
                return cache[(dice, tg)]
            res = 0
            for x in range(1, min(k, tg) + 1):
                res += rollsToTarget(dice - 1, tg - x)
            cache[(dice, tg)] = res % (10**9 + 7)
            return cache[(dice, tg)]
        cache = {}
        return rollsToTarget(n, target)

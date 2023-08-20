"""
https://leetcode.com/problems/coin-change/

Complexity
----------
Time: O(amount * coins)
Space: O(amount)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            cc = math.inf
            for c in coins:
                if amount >= c:
                    cc = min(cc, helper(amount - c) + 1)
            cache[amount] = cc
            return cc
        cc = helper(amount)
        return cc if cc < math.inf else -1

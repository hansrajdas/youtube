"""
https://leetcode.com/problems/coin-change/

Complexity
----------
Time: O(amount * coins)
Space: O(amount)
"""

import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = set()
        dq = collections.deque([0])
        cc = 0
        while dq:
            n = len(dq)
            for _ in range(n):
                a = dq.popleft()
                if a == amount:
                    return cc
                if a > amount or a in seen:
                    continue
                seen.add(a)
                for c in coins:
                    dq.append(a + c)
            cc += 1
        return -1

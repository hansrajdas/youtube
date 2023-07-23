"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Complexity
----------
Time: O(k*n)
Space: O(k*n)

Reference
---------
../_lc-0123-hard-best-time-to-buy-and-sell-stock-iii/1-top-down.py
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cache = {}
        def profit(i, isBuy, x):
            """Returns max profit earned."""
            if i == len(prices) or x == k:
                return 0
            key = (i, isBuy, x)
            if key in cache:
                return cache[key]
            if isBuy:
                cache[key] = max(
                    profit(i + 1, 1, x),  # Don't buy
                    profit(i + 1, 0, x) - prices[i])  # Buy
            else:
                cache[key] = max(
                    profit(i + 1, 0, x),  # Don't sell
                    profit(i + 1, 1, x + 1) + prices[i])  # sell
            return cache[key]
        return profit(0, 1, 0)

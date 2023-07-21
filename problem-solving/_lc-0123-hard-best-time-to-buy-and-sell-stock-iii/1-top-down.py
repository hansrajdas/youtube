"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Complexity
----------
Time: O(n)
Space: O(n)

Reference
---------
Approach-1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/796990/c-worst-to-best-solution-explained-for-dummies-like-me/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def profit(i, isBuy, k):
            if i >= len(prices) or k == 2:
                return 0
            key = (i, isBuy, k)
            if key in cache:
                return cache[key]
            if isBuy:
                cache[key] = max(
                    profit(i + 1, 1, k),  # Don't buy
                    profit(i + 1, 0, k) - prices[i])  # Buy
            else:
                cache[key] = max(
                    profit(i + 1, 0, k),  # Don't sell
                    profit(i + 1, 1, k + 1) + prices[i])  # Sell
            return cache[key]
        return profit(0, 1, 0)

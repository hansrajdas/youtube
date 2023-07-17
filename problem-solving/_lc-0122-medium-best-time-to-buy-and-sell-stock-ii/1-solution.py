"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Complexity
----------
Time: O(n)
Space: O(1)

NOTE
----
This is a peak valley problem, we have to buy and valleys and sell at peaks.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i, n = 0, 0, len(prices)
        while i < n:
            while i < n - 1 and prices[i] > prices[i + 1]:
                i += 1
            buy = prices[i]
            while i < n - 1 and prices[i] < prices[i + 1]:
                i += 1
            profit += prices[i] - buy
            i += 1
        return profit

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Complexity
----------
Time: O(n)
Space: O(1)

NOTE
----
Instead of finding peaks and valleys (as in ./1-solution.py) we can just add
increments (if we see a new price) and it will eventually the profit that can be earned.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, _min = 0, prices[0]
        for price in prices[1:]:
            if price > _min:
                profit += price - _min
            _min = price
        return profit

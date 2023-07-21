"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Complexity
----------
Time: O(n)
Space: O(n)

Reference
---------
Approach-3: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/796990/c-worst-to-best-solution-explained-for-dummies-like-me/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = math.inf
        profit1 = profit2 = -math.inf
        for i, p in enumerate(prices):
            buy1 = min(buy1, p)
            profit1 = max(profit1, p - buy1)
            buy2 = min(buy2, p - profit1)
            profit2 = max(profit2, p - buy2)
        return profit2

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        localMin = prices[0]
        for i in range(1, len(prices)):
            if diff < prices[i] - localMin:
                diff = prices[i] - localMin
            if prices[i] < localMin:
                localMin = prices[i]
        return diff

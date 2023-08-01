"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Complexity
----------
Time: O(k*n)
Space: O(k)

Reference
---------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/solutions/54125/very-understandable-solution-by-reusing-problem-iii-idea/comments/1243324
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [math.inf] * (k + 1)
        profit = [0] * (k + 1)
        for p in prices:
            for i in range(1, k + 1):
                buy[i] = min(buy[i], p - profit[i - 1])
                profit[i] = max(profit[i], p - buy[i])
        return profit[k]

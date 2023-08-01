"""
https://leetcode.com/problems/coin-change/

Complexity
----------
Time: O(amount * coins)
Space: O(amount)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a - c] + 1, dp[a])
        return -1 if dp[amount] > amount else dp[amount]

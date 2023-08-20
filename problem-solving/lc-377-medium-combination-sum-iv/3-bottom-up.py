"""
https://leetcode.com/problems/combination-sum-iv

Complexity
----------
Time: O(n*T)
Space: O(T)

n = len(nums)
T = target
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for tg in range(1, target + 1):
            for n in nums:
                if n <= tg:
                    dp[tg] += dp[tg - n]
        return dp[target]

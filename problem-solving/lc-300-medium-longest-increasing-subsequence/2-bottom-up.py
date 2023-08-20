"""
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

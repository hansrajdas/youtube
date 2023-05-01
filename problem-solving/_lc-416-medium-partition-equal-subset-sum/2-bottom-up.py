"""
https://leetcode.com/problems/partition-equal-subset-sum/

Complexity
----------
Time: O(n*S)
Space: O(n*S)

n = Number of elements in array
S = Sum of all numbers

NOTE: This can be solved with 1D array also, check solutions tab of this problem.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2:
            return False
        halfSum = S // 2
        n = len(nums)
        dp = [[False] * (halfSum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
        for s in range(1, halfSum + 1):
            dp[0][s] = False

        for i in range(1, n + 1):
            for s in range(1, halfSum + 1):
                dp[i][s] = dp[i - 1][s]
                if s >= nums[i - 1]:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - nums[i - 1]]
        return dp[n][halfSum]

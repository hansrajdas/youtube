"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Complexity
----------
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        for i in range(n):
            v = 1
            for j in range(i + 1, n):
                if nums[j - 1] >= nums[j]:
                    break
                v += 1
            ans = max(ans, v)
        return ans

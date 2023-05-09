"""
https://leetcode.com/problems/3sum/

Complexity
----------
Time: O(n^2)
Space: O(n)
"""

def twoSum(nums, tg, ans):
    seen = set()
    for v in nums:
        if tg - v in seen:
            ans.add(tuple(sorted((-tg, v, tg - v))))
        seen.add(v)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i, v in enumerate(nums):
            twoSum(nums[i + 1:], -v, ans)
        return list(ans)

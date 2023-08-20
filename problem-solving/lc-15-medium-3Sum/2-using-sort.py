"""
https://leetcode.com/problems/3sum/

Complexity
----------
Time: O(n^2)
Space: O(n)
"""

def twoSum(nums, tg, ans):
    left = 0
    right = len(nums) - 1
    while left < right:
        S = nums[left] + nums[right]
        if S == tg:
            ans.add((-tg, nums[left], nums[right]))
            left += 1
            right -= 1
        elif S > tg:
            right -= 1
        else:
            left += 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i, v in enumerate(nums):
            twoSum(nums[i + 1:], -v, ans)
        return list(ans)

"""
https://leetcode.com/problems/house-robber/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]  # Have atleast one element
        twoAway = nums[0]
        oneAway = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(nums[i] + twoAway, oneAway)
            twoAway = oneAway
            oneAway = temp
        return oneAway

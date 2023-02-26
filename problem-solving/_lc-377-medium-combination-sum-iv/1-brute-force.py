"""
https://leetcode.com/problems/combination-sum-iv

Complexity
----------
Time: 
Space: 
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        count = 0
        for n in nums:
            if n <= target:
                count += self.combinationSum4(nums, target - n)
        return count

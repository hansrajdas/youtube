"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[r] * nums[r])
                r -= 1
            else:
                res.append(nums[l] * nums[l])
                l += 1
        res.reverse()
        return res

"""
https://leetcode.com/problems/remove-element/

Complexity
----------
Time: O(n)
Space: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

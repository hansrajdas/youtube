"""
https://leetcode.com/problems/majority-element/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        c = len(nums) // 2
        for n in count:
            if count[n] > c:
                return n

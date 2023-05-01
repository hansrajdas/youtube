"""
https://leetcode.com/problems/partition-equal-subset-sum/

Complexity
----------
Time: O(n*S)
Space: O(n*S)

n = Number of elements in array
S = Sum of all elements
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2:
            return False
        cache = {}
        def isSum(idx, remSum):
            if remSum == 0:
                return True
            if idx == len(nums) or remSum < 0:
                return False
            if (idx, remSum) in cache:
                return cache[(idx, remSum)]
            cache[(idx, remSum)] = isSum(idx + 1, remSum) or isSum(idx + 1, remSum - nums[idx])
            return cache[(idx, remSum)]
        return isSum(0, S // 2)

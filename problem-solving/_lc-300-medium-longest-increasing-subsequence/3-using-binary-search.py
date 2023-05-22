"""
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(nlogn)
Space: O(n)

Explained here: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
"""

def binarySearch(nums, x):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []
        for i in range(n):
            if len(sub) == 0 or nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                idx = binarySearch(sub, nums[i])
                sub[idx] = nums[i]
        return len(sub)

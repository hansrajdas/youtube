"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Complexity
----------
Time:
  Best case: O(logn)
  Worst case: O(n) -> When all elements are same and we are searching for some other element.
Space: O(1)

Explanation: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/1890199/c-algorithm-binary-search
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # Case: [3,1,2,3,3,3,3] -> can't decide which way to go.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

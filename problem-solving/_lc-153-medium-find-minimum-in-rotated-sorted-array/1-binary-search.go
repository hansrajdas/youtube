/*
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Complexity
----------
Time:
  Best case: O(logn)
  Worst case: O(n)
Space: O(1)
*/

func findMin(nums []int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := (left + right) / 2
        if mid + 1 < len(nums) && nums[mid] > nums[mid + 1] {
            return nums[mid + 1]
        } else if nums[left] <= nums[mid] {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return nums[0]
}

/*
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Complexity
----------
Time: O(logn)
Space: O(1)
*/

func findMin(nums []int) int {
    left, right := 0, len(nums) - 1
    for left < right {
        mid := (left + right) / 2
        if nums[mid] > nums[right] {
            left = mid + 1
        } else if nums[mid] < nums[right] {
            right = mid
        } else {
            right -= 1
        }
    }
    return nums[left]
}

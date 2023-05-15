/*
https://leetcode.com/problems/sort-colors/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func sortColors(nums []int)  {
    low, mid := 0, 0
    high := len(nums) - 1
    for mid <= high {
        if nums[mid] == 0 {
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        } else if nums[mid] == 2 {
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        } else {
            mid += 1
        }
    }
}

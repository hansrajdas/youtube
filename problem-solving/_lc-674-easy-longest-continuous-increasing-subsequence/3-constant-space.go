/*
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func findLengthOfLCIS(nums []int) int {
    res := 1
    count := 1
    for i := 1; i < len(nums); i++ {
        if nums[i - 1] < nums[i] {
            count += 1
            if res < count {
                res = count
            }
        } else {
            count = 1
        }
    }
    return res
}

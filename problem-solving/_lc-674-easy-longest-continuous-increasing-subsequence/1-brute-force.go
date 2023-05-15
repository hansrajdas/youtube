/*
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(1)
*/

func findLengthOfLCIS(nums []int) int {
    lcis := 1
    n := len(nums)
    for i := 0; i < n; i++ {
        cis := 1
        for j := i + 1; j < n; j++ {
            if nums[j - 1] >= nums[j] {
                break
            }
            cis += 1
        }
        if cis > lcis {
            lcis = cis
        }
    }
    return lcis
}

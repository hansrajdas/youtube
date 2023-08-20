/*
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func findLengthOfLCIS(nums []int) int {
    n := len(nums)
    dp := make([]int, n)

    // Initialise each with 1
    for i := 0; i < n; i++ {
        dp[i] = 1
    }
    // Solve using DP
    for i := 1; i < n; i++ {
        if nums[i - 1] < nums[i] {
            dp[i] = dp[i - 1] + 1
        }
    }
    // Find max
    res := dp[0]
    for i := 1; i < n; i++ {
        if res < dp[i] {
            res = dp[i]
        }
    }
    return res
}
